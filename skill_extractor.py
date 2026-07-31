import pandas as pd
import re

def load_skills():
    skills_df=pd.read_csv("data/skill_dictionary.csv")
    skills_df.columns=skills_df.columns.str.strip()
    skills_df["Category"]=(skills_df["Category"].fillna("").astype(str).str.strip())
    skills_df["Skill"]=(skills_df["Skill"].fillna("").astype(str).str.strip())
    skills_df=skills_df[skills_df["Skill"]!=""]
    return skills_df

def extract_skills(text,skills_df):
    text=text.lower()
    found_skills=[]
    categorized_skills={}
    for _,row in skills_df.iterrows():
        category=str(row["Category"]).strip()
        skill=str(row["Skill"]).strip()
        if not skill:
            continue
        pattern=r'(?<!\w)'+re.escape(skill.lower())+r'(?!\w)'
        if re.search(pattern,text):
            if skill not in found_skills:
                found_skills.append(skill)
                if category not in categorized_skills:
                    categorized_skills[category]=[]
                categorized_skills[category].append(skill)
    if "GitHub" in found_skills and "Git" not in found_skills:
        found_skills.append("Git")
        git_category=""
        for _,row in skills_df.iterrows():
            if str(row["Skill"]).strip().lower()=="git":
                git_category=str(row["Category"]).strip()
                break
        if git_category:
            if git_category not in categorized_skills:
                categorized_skills[git_category]=[]
            categorized_skills[git_category].append("Git")
    return found_skills,categorized_skills
