from app.services.ats_engine import calculate_ats_score, get_score_label
from app.services.llm import analyze_resume_with_llm


def analyze_resume_text(resume_text: str) -> dict:
    ats_result = calculate_ats_score(resume_text)
    llm_result = analyze_resume_with_llm(resume_text)

    final_score = ats_result["final_score"]
    score_breakdown = ats_result["score_breakdown"]

    return {
        "final_score": final_score,
        "score_label": get_score_label(final_score),
        "score_breakdown": score_breakdown,
        "overall_assessment": llm_result.get(
            "overall_assessment",
            "No assessment generated."
        ),
        "top_recommendations": llm_result.get(
            "top_recommendations",
            []
        ),
        "strengths": llm_result.get(
            "strengths",
            []
        ),
        "weaknesses": llm_result.get(
            "weaknesses",
            []
        ),
        "ats_risks": llm_result.get(
            "ats_risks",
            []
        ),
    }