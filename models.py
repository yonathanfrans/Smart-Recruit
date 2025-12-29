from extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    profile = db.relationship(
        'CandidateProfile',
        backref='user',
        uselist=False,
        cascade='all, delete-orphan'
    )
    job_classification = db.relationship(
        'JobClassification',
        back_populates='user',
        uselist=False
    )


class CandidateProfile(db.Model):
    __tablename__ = 'candidate_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), nullable=True)
    address = db.Column(db.Text, nullable=True)
    instagram = db.Column(db.String(100), nullable=True)
    github = db.Column(db.String(100), nullable=True)


class JobClassification(db.Model):
    __tablename__ = 'job_classifications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)

    skills = db.Column(db.Text, nullable=False) 
    education = db.Column(db.String(100), nullable=False) 
    certification = db.Column(db.Text, nullable=False) 
    certification_files = db.Column(db.Text, nullable=True) 
    experience = db.Column(db.Text, nullable=True)
    experience_years = db.Column(db.Integer, nullable=False, default=0)
    projects = db.Column(db.Text, nullable=True)
    projects_count = db.Column(db.Integer, nullable=False, default=0)
    job_role = db.Column(db.String(100), nullable=True)

    user = db.relationship(
        'User',
        back_populates='job_classification'
    )


