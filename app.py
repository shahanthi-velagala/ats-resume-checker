import os
import io
import json
from flask import Flask, request, jsonify, render_template
from google.genai import Client
from PyPDF2 import PdfReader

app = Flask(__name__)

# ✅ Gemini client (environment variable)
client = Client(api_key="Gemini API Key")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        print("Analyze endpoint hit")

        # 1. Job Description
        job_description = request.form.get("job_description")
        if not job_description:
            return jsonify({"error": "Job description is required"}), 400

        # 2. Resume File
        if "resume" not in request.files:
            return jsonify({"error": "Resume file is required"}), 400

        resume_file = request.files["resume"]
        print("Resume file:", resume_file.filename)

        # 3. Extract PDF text
        pdf_reader = PdfReader(io.BytesIO(resume_file.read()))
        resume_text = ""

        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                resume_text += text + " "

        if len(resume_text.strip()) < 50:
            return jsonify({"error": "Unable to extract text from resume"}), 400

        # 4. Prompt
        prompt = f"""
You are an expert Application Tracking System (ATS).

Compare the RESUME with the JOB DESCRIPTION.

JOB DESCRIPTION:
{job_description}

RESUME:
{resume_text}

Return ONLY valid JSON in this exact format:
{{
  "match_percentage": 0-100,
  "match_summary": "",
  "matching_skills": [],
  "missing_skills": [],
  "improvement_suggestions": []
}}
"""

        # 5. Gemini call
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        raw_text = response.text.strip()
        print("RAW GEMINI RESPONSE:\n", raw_text)

        # 6. SAFE JSON extraction
        start = raw_text.find("{")
        end = raw_text.rfind("}") + 1

        if start == -1 or end == -1:
            raise ValueError("No JSON found in Gemini response")

        json_text = raw_text[start:end]
        print("CLEAN JSON:\n", json_text)

        result = json.loads(json_text)

        print("ANALYSIS SUCCESS")
        return jsonify(result)

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": "Analysis failed"}), 500


if __name__ == "__main__":
    app.run(port=2000, debug=True)
