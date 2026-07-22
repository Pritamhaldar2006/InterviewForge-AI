from app.embeddings.embedding_model import get_embedding_model

from app.loaders.pdf_loader import load_pdf
from app.loaders.text_loader import load_text

from app.services.indexing import create_index


def create_resume_index():

    embeddings = get_embedding_model()

    documents = load_pdf(
        "backend/data/resumes/ResumeSamrat2025.pdf"
    )

    create_index(
        documents,
        embeddings,
        "faiss_index/resume",
    )


def create_job_description_index():

    embeddings = get_embedding_model()

    documents = load_text(
        "backend/data/job_description/jd.txt"
    )

    create_index(
        documents,
        embeddings,
        "faiss_index/job_description",
    )