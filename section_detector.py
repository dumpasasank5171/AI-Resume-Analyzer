import re


def detect_sections(text):

    text_lower = text.lower()

    email_found = bool(
        re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )
    )

    phone_found = bool(
        re.search(
            r"(\+?\d{1,3}[- ]?)?(\d{10})",
            text
        )
    )

    linkedin_found = "linkedin" in text_lower
    github_found = "github" in text_lower

    detected_sections = {}

    detected_sections["Contact Information"] = (
        email_found or
        phone_found or
        linkedin_found or
        github_found
    )

    sections = {
        "Career Objective": [
            "objective",
            "career objective",
            "professional summary",
            "summary"
        ],
        "Education": [
            "education",
            "academic",
            "qualification",
            "degree"
        ],
        "Skills": [
            "skills",
            "technical skills",
            "key skills"
        ],
        "Projects": [
            "projects",
            "project"
        ],
        "Experience": [
            "experience",
            "work experience",
            "internship",
            "employment"
        ],
        "Certifications": [
            "certifications",
            "certification",
            "certificate"
        ],
        "Achievements": [
            "achievements",
            "achievement",
            "awards",
            "award"
        ],
        "Languages": [
            "languages",
            "language"
        ],
        "Interests": [
            "interests",
            "hobbies"
        ]
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