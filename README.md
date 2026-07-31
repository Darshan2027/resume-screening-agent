# 🤖 AI Resume Screening Agent

An AI-powered Resume Screening and Career Recommendation System built using Python and Streamlit. The application analyzes resumes, calculates ATS scores, identifies skill gaps, recommends companies, and provides career guidance based on selected job roles.

## 🚀 Features

- 📄 Upload Resume PDF
- 📊 ATS Score Calculation
- ✅ Matched Skills Detection
- ❌ Missing Skills Analysis
- 🏢 Company Recommendations
- 📧 Automatic Email Extraction from Resume
- 📚 Career Guidance
- 🎯 Role-Based Skill Matching
- 💡 Resume Improvement Suggestions

## 🛠️ Supported Roles

- Python Developer
- Data Analyst
- Data Scientist
- AI/ML Engineer
- DevOps Engineer

## 🧰 Technologies Used

- Python
- Streamlit
- PDFPlumber
- Regular Expressions (Regex)
- SMTP (Email Service)

## 📂 Project Structure

```text
AI-Resume-Screening-Agent/
│
├── app.py
├── requirements.txt
├── README.md
├── screenshots/
└── sample_resumes/
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Screening-Agent.git
cd AI-Resume-Screening-Agent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m streamlit run app.py
```

## 📊 How It Works

1. Select a Job Role.
2. Upload Resume PDF.
3. System extracts text from the resume.
4. Skills are matched against role requirements.
5. ATS Score is calculated.
6. Missing skills are identified.
7. Recommended companies are displayed.
8. Email address is extracted from the resume.
9. Analysis report can be sent via email.

## 📈 Example Output

### ATS Score

```text
ATS Score: 82%
```

### Matched Skills

```text
Python
SQL
Pandas
NumPy
```

### Missing Skills

```text
Power BI
Tableau
```

### Recommended Companies

```text
Amazon
Microsoft
Infosys
Accenture
```

## 🔮 Future Enhancements

- Multiple Resume Ranking
- AI-Based Resume Feedback
- Resume PDF Report Generation
- Interview Question Recommendations
- Certification Suggestions
- Resume vs Job Description Matching
- Dashboard Analytics
- Company-Wise Skill Requirements

## 📸 Screenshots

Add screenshots of your application here.

## 👨‍💻 Author

**Darshan C S**

Final Year Information Science & Engineering Student

## 📄 License

This project is developed for educational and learning purposes.