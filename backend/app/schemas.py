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
    score_breakdown: ScoreBreakdown
    overall_assessment: str
    strengths: list[str]
    weaknesses: list[str]
    improvement_suggestions: list[str]
    ats_risks: list[str]


class AnalyzeFileResponse(BaseModel):
    filename: str
    content_type: str
    extracted_text_preview: str
    analysis: ResumeAnalysis