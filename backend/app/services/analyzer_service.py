from app.services.llm import analyze_resume_with_llm


def analyze_resume_text(resume_text: str) -> dict:
    return analyze_resume_with_llm(resume_text)