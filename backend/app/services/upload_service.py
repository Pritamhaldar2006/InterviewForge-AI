from pathlib import Path
import shutil

from app.services.session_service import (
    create_session,
    get_resume_path,
    get_jd_path,
    get_resume_index_path,
    get_jd_index_path,
)

from app.loaders.pdf_loader import load_pdf
from app.loaders.text_loader import load_text

from app.vectorstore.indexing import build_vectorstore


def save_file(
    source_path: str,
    destination_path: Path,
):
    """
    Copy a file to the destination path.
    """

    source = Path(source_path)

    if not source.exists():
        raise FileNotFoundError(
            f"File not found: {source}"
        )

    destination_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    shutil.copy2(
        source,
        destination_path,
    )


def create_interview_session(
    resume_source_path: str,
    jd_source_path: str,
):
    """
    Create a complete interview session.

    Steps:
    1. Create session
    2. Save resume
    3. Save JD
    4. Build resume FAISS index
    5. Build JD FAISS index

    Returns:
        session_id
    """

    session_id = create_session()

    resume_path = get_resume_path(
        session_id
    )

    jd_path = get_jd_path(
        session_id
    )

    # Save files
    save_file(
        resume_source_path,
        resume_path,
    )

    save_file(
        jd_source_path,
        jd_path,
    )

    # Load documents
    resume_documents = load_pdf(
        str(resume_path)
    )

    jd_documents = load_text(
        str(jd_path)
    )

    # Build FAISS indexes
    build_vectorstore(
        resume_documents,
        str(
            get_resume_index_path(
                session_id
            )
        ),
    )

    build_vectorstore(
        jd_documents,
        str(
            get_jd_index_path(
                session_id
            )
        ),
    )

    return session_id