from flask import Flask, render_template, redirect, url_for, request, flash, abort, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, login_required, current_user
from functools import wraps
from extensions import db, login_manager
from models import User, CandidateProfile, JobClassification
from datetime import datetime

import joblib
import os
import numpy as np


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-anda'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # 16MB
# Config DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartrecruit.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads/profile'

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = None

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# Role Based Access
def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            if current_user.role != role:
                abort(403)
            return f(*args, **kwargs)
        return wrapped
    return decorator

# Load model ML
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, 'model')

model = joblib.load(os.path.join(MODEL_PATH, 'model.pkl'))
skills_vectorizer = joblib.load(os.path.join(MODEL_PATH, 'skills_vectorizer.pkl'))
certs_vectorizer = joblib.load(os.path.join(MODEL_PATH, 'certs_vectorizer.pkl'))
education_map = joblib.load(os.path.join(MODEL_PATH, 'education_map.pkl'))

def predict_job_role(jc):
    skills_text = jc.skills or ""
    certs_text = jc.certification or ""

    skills_vec = skills_vectorizer.transform([skills_text])
    certs_vec = certs_vectorizer.transform([certs_text])
    education_value = education_map.get(jc.education, 0)
    experience_years = jc.experience_years or 0
    projects_count = jc.projects_count or 0

    numeric_features = np.array([
        education_value,
        experience_years,
        projects_count
    ]).reshape(1, -1)

    X = np.hstack([
        skills_vec.toarray(),
        certs_vec.toarray(),
        numeric_features
    ])

    prediction = model.predict(X)

    return prediction[0]

# API Candidates
@app.route("/api/candidates", methods=["GET"])
def api_candidates():
    if request.headers.get("X-API-KEY") != "SECRET123":
        abort(401)

    candidates = (
        db.session.query(User)
        .join(CandidateProfile)
        .join(JobClassification)
        .filter(
            User.role == "candidate",
            CandidateProfile.status == "Unemployed"
        )
        .all()
    )

    result = []

    for c in candidates:
        result.append({
            "name": f"{c.profile.first_name} {c.profile.last_name}",
            "job_role": c.job_classification.job_role,
            "skills": c.job_classification.skills,
            "education": c.job_classification.education,
            "experience_years": c.job_classification.experience_years,
            "social_media": {
                "github": c.profile.github,
                "instagram": c.profile.instagram
            }
        })

    return jsonify(result)


# Routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/assistant")
@login_required
@role_required('recruiter')
def assistant():
    return render_template("assistant.html")

@app.route("/candidate")
@login_required
@role_required('recruiter')
def candidate():
    category = request.args.get("category")
    search = request.args.get("search")
    roles = request.args.getlist("role")

    CATEGORY_MAP = {
    'data-science': 'Data Scientist',
    'ai': 'AI Engineer',
    'cybersecurity': 'Cybersecurity Engineer'
    }


    query = (
        db.session.query(User)
        .join(CandidateProfile)
        .join(JobClassification)
        .filter(User.role == 'candidate', CandidateProfile.status == 'Unemployed') 
    )

    # sinkronisasi category → checkbox
    if category:
        mapped_role = CATEGORY_MAP.get(category.lower())
        if mapped_role and mapped_role not in roles:
            roles.append(mapped_role)

    roles = [r for r in roles if r in CATEGORY_MAP.values()]
    
    # Search nama kandidat
    if search:
        query = query.filter(
            db.or_(
                CandidateProfile.first_name.ilike(f"%{search}%"),
                CandidateProfile.last_name.ilike(f"%{search}%")
            )
        )

    # Filter checkbox job role
    if roles:
        query = query.filter(
            JobClassification.job_role.in_(roles)
        )

    candidates = query.all()

    return render_template(
        "candidate.html",
        candidates=candidates,
        selected_roles=roles,
        search=search,
        active_page='category'
    )

@app.route("/candidate/<string:username>")
@login_required
@role_required('recruiter')
def candidate_detail(username):
    candidate = (
        db.session.query(User)
        .join(CandidateProfile)
        .join(JobClassification)
        .filter(
            User.username == username,
            User.role == 'candidate'
        )
        .first_or_404()
    )

    return render_template(
        "detail-candidate.html", 
        candidate=candidate,
        active_page="category"
    )


@app.route("/profile", methods=["GET"])
@login_required
@role_required('candidate')
def profile():
    # Get tampilkan data
    return render_template(
        "profile.html", 
        profile=current_user.profile,
        job=current_user.job_classification,
        user=current_user
    )

@app.route("/profile/update", methods=["POST"])
@login_required
@role_required('candidate')
def update_profile():
    profile = current_user.profile
    # update username
    current_user.username = request.form['username']

    # update profile data
    profile.first_name = request.form['first_name']
    profile.last_name = request.form['last_name']
    profile.birthdate = datetime.strptime(
        request.form['birthdate'], '%Y-%m-%d'
    )
    profile.status = request.form.get('status')
    profile.address = request.form.get('address')
    profile.phone_number = request.form['phone_number']
    profile.email = request.form['email']
    profile.instagram = request.form['instagram']
    profile.github = request.form['github']

    # image upload
    image = request.files.get('image_profile')
    if image and image.filename != "":
        filename = secure_filename(image.filename)
        upload_path = os.path.join(
            app.root_path,
            'static/uploads/profile',
            filename
        )

        os.makedirs(os.path.dirname(upload_path), exist_ok=True)
        image.save(upload_path)

        profile.image = filename
        
    db.session.commit()
    flash("Profile successfully updated", "success")

    return redirect(url_for('profile'))

@app.route('/profile/job-role', methods=['POST'])
@login_required
@role_required('candidate')
def save_job_role():
    jc = current_user.job_classification

    # ambil data form
    skills = request.form['skills']
    education = request.form['education']
    certifications = request.form['certifications']
    experience = request.form.get('experience')
    experience_years = int(request.form.get('experience_years', 0))
    projects = request.form.get('projects')
    projects_count = int(request.form.get('projects_count', 0))

    # upload file sertifikat
    files = request.files.getlist('certification_files')
    filenames = []

    for file in files:
        if file and file.filename.endswith('.pdf'):
            if file.content_length > 16 * 1000 * 1000:
                flash('Each file must be under 5MB', 'warning')
                return redirect(url_for('profile'))
            
            filename = secure_filename(file.filename)
            file.save(os.path.join(
                app.root_path,
                'static/uploads/certifications', 
                filename
                ))
            filenames.append(filename)

    # insert atau update
    if jc:
        jc.skills = skills
        jc.education = education
        jc.certification = certifications
        jc.experience = experience
        jc.experience_years = experience_years
        jc.projects = projects
        jc.projects_count = projects_count
        if filenames:
            jc.certification_files = ','.join(filenames)

    else:
        jc = JobClassification(
            user_id=current_user.id,
            skills=skills,
            education=education,
            certification=certifications,
            certification_files=','.join(filenames),
            experience=experience,
            experience_years=experience_years,
            projects=projects,
            projects_count=projects_count
        )
        db.session.add(jc)

    job_role = predict_job_role(jc)
    jc.job_role = job_role

    db.session.commit()
    flash('Job role data saved successfully', 'success')
    return redirect(url_for('profile'))


# Login & Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if current_user.is_authenticated:
            abort(403)

        if User.query.filter_by(username=request.form['username']).first():
            flash("Username already registered", "warning")
            return redirect(url_for('register'))

        password = request.form['password']
        confirm = request.form['confirm_password']

        if password != confirm:
            flash("Password doesn't match", "warning")
            return redirect(url_for('register'))

        user = User(
            username=request.form['username'],
            password_hash=generate_password_hash(password),
            role='candidate'
        )

        db.session.add(user)
        db.session.flush()

        file = request.files.get('image')
        filename = None

        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        profile = CandidateProfile(
            user_id=user.id,
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            birthdate=datetime.strptime(
                request.form['birthdate'], '%Y-%m-%d'
            ),
            phone_number=request.form['phone_number'],
            email=request.form['email'],
            image=filename
        )

        db.session.add(profile)
        db.session.commit()

        flash("Registration was successful. Please log in.", "success")
        return redirect(url_for('home'))

    return render_template('register.html', active_page=None)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password_hash, password):
        login_user(user)

        if user.role == 'recruiter':
            return redirect(url_for('candidate'))
        else:
            return redirect(url_for('profile'))

    flash("Incorrect username or password", 'warning')
    return redirect(request.referrer or url_for('home'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Error Handler
@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(401)
def unauthorized(e):
    return render_template('401.html'), 401

@app.errorhandler(413)
def request_entity_too_large(error):
    flash('The file is too large. Maximum size is 16MB.', 'warning')
    return redirect(url_for('profile'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
