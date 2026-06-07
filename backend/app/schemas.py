from pydantic import BaseModel


class ScoreBreakdown(BaseModel):
    readability: int
    structure: int
    experience_clarity: int
    skills_keywords: int
    measurable_achievements: int
    language_professionalism: int


class ResumeAnalysis(BaseModel):
    final_score: int
    score_label: str
    score_breakdown: ScoreBreakdown
    overall_assessment: str
    top_recommendations: list[str]
    strengths: list[str]
    weaknesses: list[str]
    ats_risks: list[str]


class AnalyzeFileResponse(BaseModel):
    filename: str
    extracted_text_preview: str
    analysis: ResumeAnalysis
    job_match_score: int | None = None
    missing_keywords: list[str] = []
    matched_keywords: list[str] = []