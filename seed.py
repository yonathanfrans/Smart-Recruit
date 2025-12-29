from app import app
from extensions import db
from models import User
from werkzeug.security import generate_password_hash

with app.app_context():
    recruiter = User.query.filter_by(username="Recruiter01").first()

    if not recruiter:
        recruiter = User(
            username="Recruiter01",
            password_hash=generate_password_hash("recruiter123"),
            role="recruiter"
        )
        db.session.add(recruiter)
        db.session.commit()
        print("Recruiter account created successfully!")
    else:
        print("Recruiter already exists.")
