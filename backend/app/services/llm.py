import json
import requests

from app.prompts.resume_prompt import RESUME_ANALYSIS_PROMPT


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


def analyze_resume_with_llm(resume_text: str) -> dict:
    prompt = f"""
{RESUME_ANALYSIS_PROMPT}

{resume_text}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    result = response.json()

    content = result["response"]

    try:
        return json.loads(content)

    except json.JSONDecodeError:
        return {
            "final_score": 0,
            "score_breakdown": {
                "readability": 0,
                "structure": 0,
                "experience_clarity": 0,
                "skills_keywords": 0,
                "measurable_achievements": 0,
                "language_professionalism": 0
            },
            "overall_assessment": "Model returned invalid JSON.",
            "strengths": [],
            "weaknesses": [],
            "improvement_suggestions": [],
            "ats_risks": []
        }