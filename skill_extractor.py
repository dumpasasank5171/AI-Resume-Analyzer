import pandas as pd
import re


def load_skills():

    skills_df = pd.read_csv("data/skill_dictionary.csv")

    skills_df.columns = skills_df.columns.str.strip()

    skills_df["Category"] = skills_df["Category"].astype(str).str.strip()

    skills_df["Skill"] = skills_df["Skill"].astype(str).str.strip()

    return skills_df


def extract_skills(text, skills_df):

    text = text.lower()

    found_skills = []

    categorized_skills = {}

    for _, row in skills_df.iterrows():

        category = row["Category"]

        skill = row["Skill"]

        pattern = r'(?<!\w)' + re.escape(skill.lower()) + r'(?!\w)'

        if re.search(pattern, text):

            if skill not in found_skills:

                found_skills.append(skill)

                if category not in categorized_skills:

                    categorized_skills[category] = []

                categorized_skills[category].append(skill)

    found_skills.sort()

    for category in categorized_skills:

        categorized_skills[category].sort()

    return found_skills, categorized_skills