from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

UPLOAD_DIR = BASE_DIR / "uploads"

RESUME_UPLOAD_DIR = UPLOAD_DIR / "resumes"

JD_UPLOAD_DIR = UPLOAD_DIR / "job_descriptions"

INDEX_DIR = BASE_DIR / "indexes"

RESUME_INDEX_DIR = INDEX_DIR / "resumes"

JD_INDEX_DIR = INDEX_DIR / "job_descriptions"