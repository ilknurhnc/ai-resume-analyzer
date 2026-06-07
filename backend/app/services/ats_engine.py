import re


def has_keyword(text: str, keywords: list[str]) -> bool:
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in keywords)


def count_keywords(text: str, keywords: list[str]) -> int:
    text_lower = text.lower()
    return sum(1 for keyword in keywords if keyword.lower() in text_lower)


def calculate_ats_score(text: str) -> dict:
    score_breakdown = {
        "readability": calculate_readability(text),
        "structure": calculate_structure(text),
        "experience_clarity": calculate_experience_clarity(text),
        "skills_keywords": calculate_skills_keywords(text),
        "measurable_achievements": calculate_measurable_achievements(text),
        "language_professionalism": calculate_language_professionalism(text),
    }

    final_score = round(sum(score_breakdown.values()) / len(score_breakdown))

    return {
        "final_score": final_score,
        "score_breakdown": score_breakdown
    }


def calculate_readability(text: str) -> int:
    length = len(text.strip())

    if length < 500:
        return 40

    if length < 1000:
        return 60

    if length < 3000:
        return 85

    return 75


def calculate_structure(text: str) -> int:
    sections = [
        "profile",
        "summary",
        "education",
        "experience",
        "projects",
        "skills",
        "technical skills",
        "languages",
        "certifications",
    ]

    matched = count_keywords(text, sections)

    return min(40 + matched * 8, 100)


def calculate_experience_clarity(text: str) -> int:
    action_verbs = [
        "developed",
        "implemented",
        "built",
        "designed",
        "created",
        "managed",
        "contributed",
        "improved",
        "optimized",
        "configured",
        "worked",
    ]

    matched = count_keywords(text, action_verbs)

    return min(45 + matched * 7, 100)


def calculate_skills_keywords(text: str) -> int:
    technical_keywords = [
        "python",
        "java",
        "c",
        "c++",
        "javascript",
        "react",
        "sql",
        "linux",
        "git",
        "github",
        "docker",
        "api",
        "backend",
        "frontend",
        "database",
        "kubernetes",
        "fastapi",
        "machine learning",
        "mlops",
    ]

    matched = count_keywords(text, technical_keywords)

    return min(30 + matched * 5, 100)


def calculate_measurable_achievements(text: str) -> int:
    numeric_patterns = [
        r"\d+%",
        r"\d+\+",
        r"\d+ users",
        r"\d+ projects",
        r"\d+ months",
        r"\d+ years",
    ]

    metric_words = [
        "increased",
        "reduced",
        "improved",
        "optimized",
        "automated",
        "performance",
        "faster",
        "decreased",
        "saved",
    ]

    numeric_matches = sum(
        1 for pattern in numeric_patterns if re.search(pattern, text.lower())
    )

    word_matches = count_keywords(text, metric_words)

    return min(35 + numeric_matches * 10 + word_matches * 6, 100)


def calculate_language_professionalism(text: str) -> int:
    weak_phrases = [
        "i am",
        "i want",
        "hardworking",
        "responsible person",
        "i like",
    ]

    penalty = count_keywords(text, weak_phrases)

    return max(90 - penalty * 10, 50)


def get_score_label(score: int) -> str:
    if score >= 85:
        return "Excellent"

    if score >= 70:
        return "Good"

    if score >= 50:
        return "Fair"

    return "Poor"