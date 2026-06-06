RESUME_ANALYSIS_PROMPT = """
You are an ATS resume evaluation expert.

Analyze the resume and return ONLY valid JSON.

Required JSON format:

{
  "final_score": integer,
  "score_breakdown": {
    "readability": integer,
    "structure": integer,
    "experience_clarity": integer,
    "skills_keywords": integer,
    "measurable_achievements": integer,
    "language_professionalism": integer
  },
  "overall_assessment": "string",
  "strengths": ["string"],
  "weaknesses": ["string"],
  "improvement_suggestions": ["string"],
  "ats_risks": ["string"]
}

Resume:
"""