import re
def detect_sections(text):
    text_lower = text.lower()
    email_found = bool(re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text))
    phone_found = bool(re.search(
        r"\+\d{1,3}\s?\(?\d{1,4}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
        r"|\(\d{3}\)\s?\d{3}[-.\s]?\d{4}"
        r"|\d{5}\s\d{3}\s\d{3}"
        r"|\d{4}\s\d{3}\s\d{3}"
        r"|\d{3}[-.\s]\d{3}[-.\s]\d{4}"
        r"|\d{10}", text
    ))
    linkedin_found = "linkedin" in text_lower
    github_found = "github" in text_lower
    detected_sections = {}
    detected_sections["Contact Information"] = (email_found or phone_found or linkedin_found or github_found)
    sections = {
        "Career Objective": ["objective", "career objective", "career summary", "professional summary", "summary", "profile"],
        "Education": ["education", "academic", "qualification", "degree"],
        "Skills": ["skills", "technical skills", "key skills", "core competencies"],
        "Projects": ["projects", "project", "personal projects", "academic projects"],
        "Experience": ["experience", "work experience", "employment", "employment history", "professional experience", "work history", "internship", "internships", "volunteer experience", "career history", "professional background"],
        "Certifications": ["certifications", "certification", "certificate", "licenses"],
        "Achievements": ["achievements", "achievement", "awards", "award", "honors", "publications", "leadership"],
        "Languages": ["languages", "language"],
        "Interests": ["interests", "hobbies", "extracurricular", "activities"]
    }
    present_count = 1 if detected_sections["Contact Information"] else 0
    for section, keywords in sections.items():
        found = any(keyword in text_lower for keyword in keywords)
        detected_sections[section] = found
        if found:
            present_count += 1
    total_sections = len(detected_sections)
    completion = round((present_count / total_sections) * 100)
    return detected_sections, present_count, total_sections, completion
