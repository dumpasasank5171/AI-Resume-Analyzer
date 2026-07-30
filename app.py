import streamlit as st
from resume_parser import extract_text
from text_cleaner import clean_text
from skill_extractor import load_skills, extract_skills
from job_matcher import load_jobs, match_jobs
from roadmap_generator import get_roadmap
from resume_details import extract_details
from resume_score import calculate_resume_score
from resume_suggestions import generate_suggestions
from section_detector import detect_sections

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")
st.title("📄 AI Resume Analyzer")
st.write("""
Upload your resume to receive:
- Resume Score
- Resume Section Analysis
- Skill Extraction
- Job Recommendations
- Missing Skills
- Learning Roadmap
- Resume Improvement Suggestions
""")
st.markdown("---")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("Resume uploaded successfully!")
    text = extract_text(uploaded_file)
    cleaned_text = clean_text(text)
    with st.expander("View Resume Text"):
        st.write(text)
    with st.expander("View Cleaned Resume"):
        st.write(cleaned_text)

    details = extract_details(text)
    st.header("👤 Candidate Information")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Name:**", details["Name"])
        st.write("**Email:**", details["Email"])
        st.write("**Phone:**", details["Phone"])
    with c2:
        st.write("**LinkedIn:**", details["LinkedIn"])
        st.write("**GitHub:**", details["GitHub"])
        st.write("**Portfolio:**", details["Portfolio"])
    st.markdown("---")

    sections, present, total, completion = detect_sections(text)
    st.header("📑 Resume Sections")
    st.metric("Sections Present", f"{present}/{total}")
    st.progress(min(float(completion) / 100, 1.0))
    st.write(f"Resume Completeness : **{completion}%**")
    for section, status in sections.items():
        if status:
            st.success(f"🟢 {section}")
        else:
            st.info(f"⚪ {section}")
    st.markdown("---")

    skills_df = load_skills()
    skills, categorized_skills = extract_skills(cleaned_text, skills_df)
    skills.sort()
    if len(skills) == 0:
        st.error("No skills found in the resume.")
        st.stop()

    score, breakdown = calculate_resume_score(skills, details, text)
    st.header("📊 Resume Score")
    st.metric("Overall Score", f"{score}/100")
    st.progress(min(float(score) / 100, 1.0))
    st.subheader("Score Breakdown")
    for item, marks in breakdown.items():
        st.write(f"• **{item}:** {marks}")
    st.markdown("---")

    st.header("🛠 Extracted Skills")
    for category, skill_list in categorized_skills.items():
        if skill_list:
            st.subheader(category)
            cols = st.columns(4)
            for i, skill in enumerate(skill_list):
                with cols[i % 4]:
                    st.success(skill)
    st.markdown("---")

    jobs_df = load_jobs()
    results = match_jobs(skills, jobs_df)
    if results.empty:
        st.warning("No matching jobs found for your skills profile.")
        st.stop()

    top5 = results.head(5)
    best_job = top5.iloc[0]
    required_skills = [s.strip() for s in str(best_job["Skills"]).split(",") if s.strip()]
    resume_skill_set = {skill.lower() for skill in skills}
    missing_skills = [s for s in required_skills if s.lower() not in resume_skill_set]
    roadmap = get_roadmap(missing_skills)
    suggestions = generate_suggestions(details, text, skills, missing_skills)

    st.header("🏆 Top 5 Recommended Jobs")
    for _, row in top5.iterrows():
        try:
            score_val = float(row["Score"])
        except (ValueError, TypeError):
            score_val = 0
        st.subheader(f"💼 {row['Job Role']}")
        st.progress(min(score_val / 100, 1.0))
        st.metric("Match Score", f"{score_val:.2f}%")
        job_skills = [s.strip() for s in str(row["Skills"]).split(",") if s.strip()]
        cols = st.columns(5)
        for i, skill in enumerate(job_skills):
            with cols[i % 5]:
                if skill.lower() in resume_skill_set:
                    st.success(f"✓ {skill}")
                else:
                    st.info(skill)
    st.markdown("---")
    try:
        best_score = float(best_job["Score"])
    except (ValueError, TypeError):
        best_score = 0
    st.success(f"⭐ Best Recommended Job: {best_job['Job Role']} ({best_score:.2f}%)")

    st.header("❌ Missing Skills")
    if len(missing_skills) == 0:
        st.success("Your resume already contains all required skills for the best matching job.")
    else:
        cols = st.columns(4)
        for i, skill in enumerate(missing_skills):
            with cols[i % 4]:
                st.error(skill)
    st.markdown("---")

    st.header("📚 Personalized Learning Roadmap")
    if len(missing_skills) == 0:
        st.success("No roadmap required. Your resume already covers all required skills.")
    else:
        for skill, guide in zip(missing_skills, roadmap):
            st.subheader(f"📌 {skill}")
            for step_no, step in enumerate(guide, start=1):
                st.markdown(f"{step_no}. {step}")
            st.markdown("---")

    st.header("💡 Resume Suggestions")
    if len(suggestions) == 0:
        st.success("Excellent! No suggestions at the moment.")
    else:
        for suggestion in suggestions:
            st.info(suggestion)
    st.markdown("---")

    st.header("📈 Resume Overview")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Skills Found", len(skills))
    with c2:
        st.metric("Missing Skills", len(missing_skills))
    with c3:
        st.metric("Best Match", f"{best_score:.2f}%")

    st.markdown("""
    ---
    <div style="text-align:center;color:gray;">
        <h4>AI Resume Analyzer</h4>
        Built using Streamlit, Python, and Scikit-learn <br><br>
        Resume Parsing • Skill Extraction • Resume Scoring <br>
        Job Recommendation • Skill Gap Analysis • Learning Roadmap
    </div>
    """, unsafe_allow_html=True)
