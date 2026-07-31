import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_jobs():

    jobs_df = pd.read_csv("data/job_roles.csv")

    jobs_df.columns = jobs_df.columns.str.strip()

    jobs_df["Job Role"] = jobs_df["Job Role"].astype(str).str.strip()

    jobs_df["Skills"] = jobs_df["Skills"].astype(str).str.strip()

    return jobs_df


def match_jobs(found_skills, jobs_df):

    resume_text = " ".join(skill.lower() for skill in found_skills)

    scores = []

    for _, row in jobs_df.iterrows():

        required_skills = [
            skill.strip()
            for skill in row["Skills"].split(",")
            if skill.strip()
        ]

        matched = 0

        found = [s.lower() for s in found_skills]

            for skill in required_skills:
                if skill.lower() in found:
                    matched += 1

        skill_score = matched / len(required_skills)

        job_text = " ".join(required_skills).lower()

        vectorizer = TfidfVectorizer()

        tfidf = vectorizer.fit_transform([resume_text, job_text])

        tfidf_score = cosine_similarity(tfidf[0], tfidf[1])[0][0]

        final_score = (0.7 * skill_score) + (0.3 * tfidf_score)

        scores.append(round(final_score * 100, 2))

    result = jobs_df.copy()

    result["Score"] = scores

    result = result.sort_values(
        by="Score",
        ascending=False
    ).reset_index(drop=True)

    return result
