def has_any(text: str, keywords: list[str]) -> bool:
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in keywords)


def count_matches(text: str, keywords: list[str]) -> int:
    text_lower = text.lower()
    return sum(1 for keyword in keywords if keyword.lower() in text_lower)


def calculate_readability_score(text: str) -> int:
    if len(text.strip()) < 500:
        return 6

    score = 10

    if len(text) > 1000:
        score += 2

    if len(text) > 2000:
        score += 2

    if "\n" in text:
        score += 1

    return min(score, 15)


def calculate_structure_score(text: str) -> int:
    sections = [
        "profile",
        "summary",
        "education",
        "experience",
        "projects",
        "technical skills",
        "skills",
        "languages"
    ]

    matched_sections = count_matches(text, sections)

    return min(matched_sections * 3, 20)


def calculate_experience_score(text: str) -> int:
    experience_keywords = [
        "experience",
        "intern",
        "worked",
        "developed",
        "implemented",
        "contributed",
        "built",
        "designed"
    ]

    matched = count_matches(text, experience_keywords)

    return min(8 + matched * 2, 20)


def calculate_skills_score(text: str) -> int:
    skill_keywords = [
        "python",
        "java",
        "c",
        "c++",
        "linux",
        "git",
        "github",
        "docker",
        "docker compose",
        "api",
        "backend",
        "frontend",
        "database",
        "kubernetes",
        "fastapi",
        "machine learning",
        "mlops"
    ]

    matched = count_matches(text, skill_keywords)

    return min(matched * 2, 20)


def calculate_achievements_score(text: str) -> int:
    achievement_indicators = [
        "%",
        "increased",
        "reduced",
        "improved",
        "optimized",
        "automated",
        "users",
        "performance",
        "faster",
        "decreased"
    ]

    matched = count_matches(text, achievement_indicators)

    return min(5 + matched * 2, 15)


def calculate_language_score(text: str) -> int:
    weak_phrases = [
        "i am",
        "i want",
        "hardworking",
        "responsible person"
    ]

    penalty = count_matches(text, weak_phrases)

    return max(10 - penalty * 2, 5)


def analyze_resume_text(resume_text: str) -> dict:
    score_breakdown = {
        "readability": calculate_readability_score(resume_text),
        "structure": calculate_structure_score(resume_text),
        "experience_clarity": calculate_experience_score(resume_text),
        "skills_keywords": calculate_skills_score(resume_text),
        "measurable_achievements": calculate_achievements_score(resume_text),
        "language_professionalism": calculate_language_score(resume_text)
    }

    final_score = sum(score_breakdown.values())

    strengths = []
    weaknesses = []
    suggestions = []
    ats_risks = []

    if score_breakdown["structure"] >= 15:
        strengths.append("The resume includes a clear section-based structure.")
    else:
        weaknesses.append("The resume structure could be clearer with standard section headings.")
        suggestions.append("Use standard headings such as Profile, Education, Experience, Projects, Skills, and Languages.")

    if score_breakdown["skills_keywords"] >= 15:
        strengths.append("The resume contains a strong set of technical keywords.")
    else:
        weaknesses.append("The resume does not contain enough technical or ATS-relevant keywords.")
        suggestions.append("Add more role-relevant technical keywords naturally into the skills and project sections.")

    if score_breakdown["experience_clarity"] >= 15:
        strengths.append("The resume includes action-oriented experience and project descriptions.")
    else:
        weaknesses.append("Experience and project descriptions could be more action-oriented.")
        suggestions.append("Start bullet points with verbs such as Built, Implemented, Designed, Optimized, or Automated.")

    if score_breakdown["measurable_achievements"] < 10:
        weaknesses.append("The resume has limited measurable achievements.")
        suggestions.append("Add numbers, percentages, performance gains, user counts, or concrete project outcomes.")
        ats_risks.append("Lack of measurable achievements may make the resume less competitive.")

    if score_breakdown["readability"] >= 12:
        strengths.append("The resume text is readable and sufficiently detailed.")
    else:
        weaknesses.append("The resume may be too short or difficult to parse.")

    if final_score >= 80:
        overall_assessment = "The resume is highly ATS-friendly and has a strong technical foundation."
    elif final_score >= 65:
        overall_assessment = "The resume is moderately ATS-friendly but needs clearer achievements and stronger keyword coverage."
    else:
        overall_assessment = "The resume needs significant improvement in structure, keyword coverage, and measurable impact."

    return {
        "final_score": final_score,
        "score_breakdown": score_breakdown,
        "overall_assessment": overall_assessment,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "improvement_suggestions": suggestions,
        "ats_risks": ats_risks
    }