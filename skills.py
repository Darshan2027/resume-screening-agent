SKILLS = [
    "python",
    "java",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "django",
    "flask",
    "fastapi",
    "mysql",
    "git",
    "github",
    "machine learning",
    "data analytics",
    "excel",
    "power bi"
]


def extract_skills(text):
    found = []

    text = text.lower()

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return found