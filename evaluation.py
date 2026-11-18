
import re

def clean_text(text):
    """Convert text to lowercase and extract words."""
    return set(re.findall(r"\b\w+\b", text.lower()))


def evaluate_answer(question, expected_answer, ai_answer):

    expected_words = clean_text(expected_answer)
    ai_words = clean_text(ai_answer)

    if not expected_words:
        return {
            "relevance": "Not evaluated",
            "completeness": "Not evaluated",
            "keyword_coverage": 0,
            "missing_information": "No expected answer provided",
            "extra_keywords": "Not evaluated"
        }

    common_words = expected_words.intersection(ai_words)
    missing_words = expected_words - ai_words
    extra_words = ai_words - expected_words

    coverage = len(common_words) / len(expected_words) * 100

    if coverage >= 70:
        relevance = "Good keyword match"
        completeness = "Good keyword coverage"
    elif coverage >= 30:
        relevance = "Partial keyword match"
        completeness = "Some expected keywords are missing"
    else:
        relevance = "Low keyword match"
        completeness = "Needs manual review"

    return {
        "relevance": relevance,
        "completeness": completeness,
        "keyword_coverage": round(coverage, 2),
        "missing_information": ", ".join(sorted(missing_words)),
        "extra_keywords": ", ".join(sorted(extra_words))
    }
