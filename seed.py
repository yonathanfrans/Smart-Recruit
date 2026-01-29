from app import app
from extensions import db
from models import User
from werkzeug.security import generate_password_hash

# Data Dummy Recruiter
RECRUITERS = [
    {"username": "Recruiter01", "password": "recruiter123"},
    {"username": "Recruiter02", "password": "recruiter456"},
    {"username": "Recruiter03", "password": "recruiter789"},
    {"username": "Recruiter04", "password": "recruiter098"},
]

# Data Dummy Candidate
# CANDIDATE = [
#     {"username": "johncena", "password": "testuser123"},
#     {"username": "cristiano7", "password": "siu777"},
#     {"username": "kylianmbappe", "password": "testuser345"},
#     {"username": "elonmuskX", "password": "undefined"},
#     {"username": "lionelmessi10", "password": "messi123"},
#     {"username": "hayleywilliams", "password": "hayley123"},
#     {"username": "billieeilish", "password": "eilish123"},
#     {"username": "adelelaurie", "password": "adele123"},
#     {"username": "amylee001", "password": "amylee123"},
#     {"username": "taylorswift", "password": "swift123"},
#     {"username": "oliviarodrigo", "password": "olivia123"},
#     {"username": "coreytaylor", "password": "corey123"},
#     {"username": "gerardway", "password": "gerard123"},
#     {"username": "oliversykes", "password": "oliver123"},
#     {"username": "harrymaguire", "password": "maguire123"},
#     {"username": "liamgallagher", "password": "liam123"},
#     {"username": "ellatoone", "password": "ella123"},
#     {"username": "bernadyaribka", "password": "bernadya123"},
#     {"username": "lilasikuta", "password": "lilas123"},

# ]

with app.app_context():
    for r in RECRUITERS:
        exists = User.query.filter_by(username=r["username"]).first()
        if not exists:
            user = User(
                username=r["username"],
                password_hash=generate_password_hash(r["password"]),
                role="recruiter"
            )
            db.session.add(user)

    db.session.commit()
    print("Recruiter dummy accounts seeded.")
