import streamlit as st
import pdfplumber
import re
import smtplib
from email.mime.text import MIMEText

# =========================
# Job Roles Database
# =========================

job_roles = {
    "Python Developer": {
        "skills": [
            "python", "oops", "sql", "django",
            "flask", "git", "html", "css", "javascript"
        ],
        "companies": [
            "Amazon", "Infosys", "TCS",
            "Wipro", "Accenture"
        ]
    },

    "Data Analyst": {
        "skills": [
            "python", "sql", "pandas", "numpy",
            "excel", "power bi", "tableau",
            "data cleaning"
        ],
        "companies": [
            "Deloitte", "EY", "KPMG",
            "Accenture", "Capgemini"
        ]
    },

    "Data Scientist": {
        "skills": [
            "python", "machine learning",
            "deep learning", "tensorflow",
            "pytorch", "statistics"
        ],
        "companies": [
            "Google", "Microsoft",
            "Amazon", "IBM"
        ]
    },

    "AI/ML Engineer": {
        "skills": [
            "python", "machine learning",
            "deep learning", "tensorflow",
            "pytorch", "nlp", "llm",
            "generative ai"
        ],
        "companies": [
            "Google", "Microsoft",
            "OpenAI", "NVIDIA"
        ]
    },

    "DevOps Engineer": {
        "skills": [
            "linux", "docker", "kubernetes",
            "jenkins", "aws", "terraform"
        ],
        "companies": [
            "Amazon", "Microsoft",
            "IBM", "Oracle"
        ]
    }
}

# =========================
# PDF Text Extraction
# =========================

def extract_text(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text.lower()

# =========================
# Email Extraction
# =========================

def extract_email(text):
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    match = re.search(pattern, text)

    if match:
        return match.group(0)

    return None

# =========================
# Email Sender
# =========================

def send_email(receiver_email, subject, body):

    try:
        sender_email = "yourgmail@gmail.com"
        app_password = "your_app_password"

        msg = MIMEText(body)

        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)

        print("Email sent successfully")

    except Exception as e:
        print("Error:", e)
    

# =========================
# Streamlit UI
# =========================

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Screening Agent")

selected_role = st.selectbox(
    "Select Job Role",
    list(job_roles.keys())
)

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# =========================
# Resume Analysis
# =========================

if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.error("Please upload a resume")
        st.stop()

    resume_text = extract_text(uploaded_file)

    candidate_email = extract_email(resume_text)

    if candidate_email:
        st.success(f"Email Found: {candidate_email}")
    else:
        st.warning("No email found in resume")

    required_skills = job_roles[selected_role]["skills"]
    companies = job_roles[selected_role]["companies"]

    matched_skills = []

    for skill in required_skills:
        if skill.lower() in resume_text:
            matched_skills.append(skill)

    missing_skills = []

    for skill in required_skills:
        if skill.lower() not in resume_text:
            missing_skills.append(skill)

    score = (
        len(matched_skills) / len(required_skills)
    ) * 100

    st.subheader("📊 Resume Analysis")

    st.metric(
        "ATS Score",
        f"{score:.2f}%"
    )

    st.write("✅ Matched Skills")
    st.write(matched_skills)

    st.write("❌ Missing Skills")
    st.write(missing_skills)

    st.write("🏢 Recommended Companies")
    st.write(companies)

    # Report
    report = f"""
Resume Analysis Report

ATS Score: {score:.2f}%

Matched Skills:
{', '.join(matched_skills)}

Missing Skills:
{', '.join(missing_skills)}

Recommended Companies:
{', '.join(companies)}
"""

    # Profile Rating
    if score >= 80:
        st.success(
            "Excellent Profile! Ready for top companies."
        )

    elif score >= 60:
        st.warning(
            "Good Profile! Improve missing skills."
        )

    else:
        st.error(
            "Need more skills before applying."
        )

    # Send Email
    if st.button("📧 Send Analysis Report"):

        if candidate_email:

            send_email(
                
                candidate_email,
                "Resume Analysis Report",
                report
            )

            st.success(
                f"Report sent to {candidate_email}"
            )

        else:
            st.error(
                "No email found in resume"
            )