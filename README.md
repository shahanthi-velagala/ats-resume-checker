# 📄 ATS Resume Checker

An **ATS (Applicant Tracking System) Resume Checker** built using Python and Generative AI.  
This project analyzes resumes against job descriptions and provides feedback, keyword matching, and improvement suggestions to help resumes perform better in ATS-based screenings.

---

## ✨ Project Overview

Most companies use **Applicant Tracking Systems (ATS)** to filter resumes before they reach recruiters.  
This project helps users understand how well their resume matches a given job description and highlights areas for improvement.

The ATS Resume Checker:
- Extracts text from resumes
- Compares resumes with job descriptions
- Calculates an ATS-style matching score
- Provides AI-generated feedback and suggestions

This project was developed as part of **Generative AI training** to understand:
- Resume parsing and analysis
- Text comparison techniques
- Generative AI integration
- Backend processing with Python
- Dependency and environment management
- GitHub project workflow

---

## 🚀 Features

- Resume text analysis
- Job description comparison
- ATS-style score calculation
- Keyword matching and missing keyword identification
- AI-powered feedback and suggestions
- Beginner-friendly and modular project structure

---

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **AI Integration:** Generative AI (Gemini API)  
- **Backend:** Python-based logic (Flask if applicable)  
- **Resume Processing:** Text extraction and analysis  
- **Environment Management:** Miniconda, Python Virtual Environment (`.venv`)  
- **Version Control:** Git & GitHub  

---

## 🧪 Environment & Setup Details

### 🔹 Miniconda
- Miniconda is used to manage the base Python environment.
- The project runs inside the Conda base environment for stability.

### 🔹 Python Virtual Environment
- A Python virtual environment (`.venv`) is used to isolate project dependencies.
- This prevents conflicts with system-wide Python packages.

---

## ⚙️ How to Run the Project Locally

Follow the steps below to run the ATS Resume Checker on your system.

---

### 1️⃣ Clone the Repository


git clone https://github.com/shahanthi-velagala/ats-resume-checker.git


cd ats-resume-checker

2️⃣ Create Virtual Environment


python -m venv .venv

3️⃣ Activate Virtual Environment

Windows (PowerShell):

.venv\Scripts\Activate.ps1


After activation, your terminal will display:

(.venv)

4️⃣ Install Required Libraries


pip install flask google-genai PyPDF2



5️⃣ Run the Application


python main.py

---

📝 Notes

This project is intended for learning and demonstration purposes.

ATS scoring logic is a simplified simulation of real-world ATS systems.

The goal is to help users improve resumes, not to replace professional ATS tools.

Future enhancements may include UI improvements, PDF upload support, and advanced scoring algorithms.
