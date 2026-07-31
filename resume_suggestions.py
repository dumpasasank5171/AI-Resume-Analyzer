def generate_suggestions(details,text,skills,missing_skills):
    suggestions=[]
    text_lower=text.lower()
    if details["Email"]=="Not Found":
        suggestions.append("Add a professional email address.")
    if details["Phone"]=="Not Found":
        suggestions.append("Add your contact number.")
    if details["LinkedIn"]=="Not Found":
        suggestions.append("Add your LinkedIn profile.")
    if details["GitHub"]=="Not Found":
        suggestions.append("Add your GitHub profile to showcase projects.")
    if details["Portfolio"]=="Not Found":
        suggestions.append("Consider adding a portfolio website.")
    education_keywords=[
        "b.tech","b.e","bachelor",
        "m.tech","m.e","master",
        "bca","mca",
        "b.sc","m.sc",
        "degree"
    ]
    if not any(word in text_lower for word in education_keywords):
        suggestions.append("Include your educational qualifications.")
    project_keywords=[
        "project",
        "projects",
        "developed",
        "implemented",
        "built"
    ]
    if not any(word in text_lower for word in project_keywords):
        suggestions.append("Add academic or personal projects.")
    experience_keywords=[
        "experience",
        "internship",
        "intern",
        "worked",
        "employment"
    ]
    if not any(word in text_lower for word in experience_keywords):
        suggestions.append("Mention internships or work experience if available.")
    certification_keywords=[
        "certification",
        "certifications",
        "certificate",
        "certified"
    ]
    if not any(word in text_lower for word in certification_keywords):
        suggestions.append("Add relevant certifications.")
    achievement_keywords=[
        "achievement",
        "achievements",
        "award",
        "awards",
        "won",
        "winner",
        "published",
        "patent",
        "recognition",
        "honor",
        "honours",
        "dean's list",
        "scholarship",
        "gpa",
        "increased",
        "improved",
        "reduced",
        "boosted",
        "optimized",
        "saved",
        "grew",
        "achieved",
        "raised",
        "%",
        "million",
        "thousand",
        "k ",
        "$"
    ]
    if not any(word in text_lower for word in achievement_keywords):
        suggestions.append("Mention your achievements or awards.")
    if len(skills)<10:
        suggestions.append("Include more technical skills relevant to your target role.")
    if len(missing_skills)>0:
        suggestions.append("Learn these missing skills: "+", ".join(missing_skills))
    return suggestions
