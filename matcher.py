import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# A reasonably broad tech/soft-skill vocabulary to check for explicitly.
# Swap/extend this list for other domains (marketing, finance, etc.) if needed.
SKILLS_DB = [
    "python", "java", "c++", "javascript", "sql", "r", "html", "css",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "keras",
    "machine learning", "deep learning", "nlp", "natural language processing",
    "data analysis", "data visualization", "data engineering", "data science",
    "streamlit", "flask", "django", "fastapi", "react", "node.js",
    "power bi", "tableau", "excel", "plotly", "matplotlib",
    "git", "github", "docker", "kubernetes", "aws", "azure", "google cloud",
    "rest api", "api integration", "database", "mysql", "postgresql", "mongodb", "sqlite",
    "agile", "scrum", "communication", "team collaboration", "problem solving",
    "project management", "leadership", "oop", "object-oriented programming",
    "data structures", "algorithms", "dsa", "statistics", "linux", "arduino", "iot",
]


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\+\#\.]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def compute_match_score(resume_text: str, jd_text: str) -> float:
    """TF-IDF + cosine similarity between the full resume and the full JD, 0-100."""
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform([clean_text(resume_text), clean_text(jd_text)])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 1)


def find_skills(text: str) -> set:
    cleaned = clean_text(text)
    found = set()
    for skill in SKILLS_DB:
        pattern = r"(?<![a-z0-9])" + re.escape(skill) + r"(?![a-z0-9])"
        if re.search(pattern, cleaned):
            found.add(skill)
    return found


def analyze(resume_text: str, jd_text: str) -> dict:
    score = compute_match_score(resume_text, jd_text)
    resume_skills = find_skills(resume_text)
    jd_skills = find_skills(jd_text)

    matched = sorted(resume_skills & jd_skills)
    missing = sorted(jd_skills - resume_skills)
    extra = sorted(resume_skills - jd_skills)

    return {
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "extra_skills": extra,
    }