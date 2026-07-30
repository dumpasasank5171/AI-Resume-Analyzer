def calculate_resume_score(skills, details, text):

    score = 0

    breakdown = {}

    skill_count = len(skills)

    if skill_count >= 15:
        skill_score = 40
    elif skill_count >= 10:
        skill_score = 30
    elif skill_count >= 5:
        skill_score = 20
    elif skill_count >= 1:
        skill_score = 10
    else:
        skill_score = 0

    score += skill_score
    breakdown["Skills"] = skill_score

    text_lower = text.lower()

    education_keywords = [
        "b.tech", "b.e", "bachelor",
        "m.tech", "m.e", "master",
        "bca", "mca",
        "b.sc", "m.sc",
        "degree"
    ]

    education_score = 15 if any(word in text_lower for word in education_keywords) else 0

    score += education_score
    breakdown["Education"] = education_score

    project_keywords = [
        "project",
        "projects",
        "developed",
        "built",
        "implemented"
    ]

    project_score = 15 if any(word in text_lower for word in project_keywords) else 0

    score += project_score
    breakdown["Projects"] = project_score

    experience_keywords = [
        "experience",
        "internship",
        "intern",
        "worked",
        "employment"
    ]

    experience_score = 15 if any(word in text_lower for word in experience_keywords) else 0

    score += experience_score
    breakdown["Experience"] = experience_score

    contact_score = 0

    if details["Email"] != "Not Found":
        contact_score += 5

    if details["Phone"] != "Not Found":
        contact_score += 5

    score += contact_score
    breakdown["Contact"] = contact_score

    profile_score = 0

    if details["GitHub"] != "Not Found":
        profile_score += 2.5

    if details["LinkedIn"] != "Not Found":
        profile_score += 2.5

    score += profile_score
    breakdown["Profiles"] = profile_score

    score = round(score)

    return score, breakdown