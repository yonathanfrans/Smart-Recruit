# List of skills
SKILLS_BY_ROLE = {
    "Data Scientist": [
        "Python",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "Keras",
        "Pytorch",
        "Pandas",
        "NLP",
        "Statistics",
        "Tableau",
        "Big Data",
        "Algorithms",
        "Data Visualization",
        "Data Analysis",
        "Data Mining",
        "Data Warehousing",
        "ETL",
        "Linux",
        "Excel",
        "Financial Analysis",
        "Digital Marketing",
        "Econometrics",
        "JavaScript",
        "Java",
        "React",
        "Node JS",
        "R",
        "HTML",
        "CSS",
        "C#",
        "C++",
        "IoT",
        ".NET",        
        "SEO",
        "Software Design",
        "Content Creation"
    ],
    "AI Engineer": [
        "Python",
        "TensorFlow",
        "Pytorch",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "Data Science",
        "Statistics",
        "HTML",
        "CSS",
        "JavaScript",
        "Algorithms",
        "Data Structures",
        "Java",
        "Automation",
        "DevOps",
        "Cloud Computing"
    ],
    "Cybersecurity Engineer": [
        "Linux",
        "Python",
        "Cybersecurity",
        "Networking",
        "Network Security",
        "Ethical Hacking",
        "Penetration Testing",
        "Cryptography",
        "Firewalls",
        "SIEM",
        "JavaScript",
        "React",
        "Node JS",
        "C++",
        "IoT",
        "Embedded Systems"
    ]
}

# Sorting Skills
def get_all_skills_sorted():
    all_skills = set()

    for skills in SKILLS_BY_ROLE.values():
        for skill in skills:
            all_skills.add(skill)

    return sorted(all_skills)

# Education Mapping
EDUCATION_OPTIONS = [
    {"label": "Sarjana (S1) Sains", "value": "B.Sc"},
    {"label": "Sarjana (S1) Teknologi", "value": "B.Tech"},
    {"label": "Sarjana (S1)", "value": "Bachelor's"},
    {"label": "Sarjana (S1) Statistika", "value": "Bachelor's in Statistics"},
    {"label": "Sarjana (S1) Keamanan Siber", "value": "Bachelor's in Cybersecurity"},

    {"label": "Magister (S2) Administrasi Bisnis", "value": "MBA"},
    {"label": "Magister (S2) Teknologi", "value": "M.Tech"},
    {"label": "Magister (S2)", "value": "Master's"},
    {"label": "Magister (S2) Ilmu Data", "value": "Master's in Data Science"},
    {"label": "Magister (S2) Keamanan Siber", "value": "Master's in Cybersecurity"},

    {"label": "Doktor (S3)", "value": "PhD"},
    {"label": "Doktor (S3) Kecerdasan Buatan", "value": "PhD in Artificial Intelligence"},
]

EDUCATION_LABEL_MAP = {
    "B.Sc": "Sarjana (S1) Sains",
    "B.Tech": "Sarjana (S1) Teknologi",
    "Bachelor's": "Sarjana (S1)",
    "Bachelor's in Statistics": "Sarjana (S1) Statistika",
    "Bachelor's in Cybersecurity": "Sarjana (S1) Keamanan Siber",

    "MBA": "Magister (S2) Administrasi Bisnis",
    "M.Tech": "Magister (S2) Teknologi",
    "Master's": "Magister (S2)",
    "Master's in Data Science": "Magister (S2) Ilmu Data",
    "Master's in Cybersecurity": "Magister (S2) Keamanan Siber",

    "PhD": "Doktor (S3)",
    "PhD in Artificial Intelligence": "Doktor (S3) Kecerdasan Buatan",
}

