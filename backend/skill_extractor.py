import json
import re


# Load skills once (performance optimization)
with open("../dataset/skills.json", "r") as f:
    SKILLS_DB = json.load(f)["skills"]


def clean_text(text: str) -> str:
    """
    Normalize text for better matching
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9+#.\s]', ' ', text)  # keep +, #, .
    return text


def extract_skills(text: str) -> list:
    """
    Extract skills from resume text
    """
    cleaned_text = clean_text(text)

    found_skills = set()

    for skill in SKILLS_DB:
        # exact word match (important!)
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        
        if re.search(pattern, cleaned_text):
            found_skills.add(skill)

    return sorted(list(found_skills))