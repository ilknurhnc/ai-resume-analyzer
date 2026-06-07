import re


COMMON_TECH_KEYWORDS = [
    "python", "java", "javascript", "typescript", "react", "node.js",
    "fastapi", "django", "flask", "sql", "postgresql", "mysql",
    "mongodb", "docker", "kubernetes", "git", "github", "linux",
    "aws", "azure", "gcp", "rest api", "api", "html", "css",
    "machine learning", "mlops", "ci/cd", "agile", "scrum"
]


def normalize_text(text: str) -> str:
    return text.lower()


def extract_keywords(text: str) -> list[str]:
    normalized = normalize_text(text)

    found_keywords = []

    for keyword in COMMON_TECH_KEYWORDS:
        pattern = r"\b" + re.escape(keyword.lower()) + r"\b"

        if re.search(pattern, normalized):
            found_keywords.append(keyword)

    return found_keywords


def calculate_job_match(resume_text: str, job_description: str) -> dict:
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)

    if not job_keywords:
        return {
            "job_match_score": 0,
            "matched_keywords": [],
            "missing_keywords": []
        }

    matched_keywords = [
        keyword for keyword in job_keywords
        if keyword in resume_keywords
    ]

    missing_keywords = [
        keyword for keyword in job_keywords
        if keyword not in resume_keywords
    ]

    job_match_score = round(
        (len(matched_keywords) / len(job_keywords)) * 100
    )

    return {
        "job_match_score": job_match_score,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords
    }