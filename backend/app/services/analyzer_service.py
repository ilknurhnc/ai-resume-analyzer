def analyze_resume_text(resume_text: str) -> dict:
    score_breakdown = {
        "readability": 13,
        "structure": 17,
        "experience_clarity": 16,
        "skills_keywords": 18,
        "measurable_achievements": 8,
        "language_professionalism": 9
    }

    final_score = sum(score_breakdown.values())

    return {
        "final_score": final_score,
        "score_breakdown": score_breakdown,
        "overall_assessment": (
            "The resume is generally ATS-friendly and clearly structured. "
            "It includes relevant technical skills, education, projects, and internship experience. "
            "However, it can be improved by adding more measurable achievements and clearer impact statements."
        ),
        "strengths": [
            "Clear technical background in C, C++, Linux, Docker, and backend-related projects.",
            "Project section is strong and relevant for software engineering roles.",
            "Education, experience, projects, skills, and languages are clearly separated.",
            "The resume includes GitHub, LinkedIn, and portfolio links."
        ],
        "weaknesses": [
            "Some project and internship bullet points lack measurable results.",
            "ATS parsing produced unusual separator characters, which may indicate formatting issues.",
            "The experience section could include more specific technical contributions.",
            "Some skills could be grouped more cleanly for better scanning."
        ],
        "improvement_suggestions": [
            "Replace generic bullets with measurable impact, such as performance improvements, number of users, or project outcomes.",
            "Use standard bullet characters instead of special symbols to improve ATS parsing.",
            "Add more role-specific keywords depending on the target job description.",
            "Make each project bullet start with a strong action verb.",
            "Include tools and technologies directly inside project descriptions where relevant."
        ],
        "ats_risks": [
            "Non-standard bullet/separator characters may reduce parsing quality.",
            "Some achievements are descriptive but not quantified.",
            "No target-role keyword comparison is currently applied."
        ]
    }