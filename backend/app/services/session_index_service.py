from app.loaders.pdf_loader import load_pdf
from app.loaders.text_loader import load_text

from app.services.session_service import (
    get_resume_path,
    get_jd_path,
    get_resume_index_path,
    get_jd_index_path,
)

from app.vectorstore.indexing import build_vectorstore


def build_session_indexes(
    session_id: str,
):
    # ---------------------------------------------
    # Paths
    # ---------------------------------------------

    resume_path = get_resume_path(
        session_id
    )

    jd_path = get_jd_path(
        session_id
    )

    resume_index_path = get_resume_index_path(
        session_id
    )

    jd_index_path = get_jd_index_path(
        session_id
    )

    # ---------------------------------------------
    # Validate files
    # ---------------------------------------------

    if not resume_path.exists():
        raise FileNotFoundError(
            f"Resume not found: {resume_path}"
        )

    if not jd_path.exists():
        raise FileNotFoundError(
            f"Job description not found: {jd_path}"
        )

    # ---------------------------------------------
    # Load documents
    # ---------------------------------------------

    resume_documents = load_pdf(
        str(resume_path)
    )

    jd_documents = load_text(
        str(jd_path)
    )

    # ---------------------------------------------
    # Build resume index
    # ---------------------------------------------

    build_vectorstore(
        documents=resume_documents,
        save_path=str(resume_index_path),
    )

    # ---------------------------------------------
    # Build JD index
    # ---------------------------------------------

    build_vectorstore(
        documents=jd_documents,
        save_path=str(jd_index_path),
    )

    return {
        "resume_index": str(
            resume_index_path
        ),
        "jd_index": str(
            jd_index_path
        ),
    }