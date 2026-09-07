from pathlib import Path
import uuid

BASE_STORAGE = Path("storage/sessions")


def create_session() -> str:
    """
    Create a new interview session.
    """

    session_id = str(uuid.uuid4())

    session_path = BASE_STORAGE / session_id

    session_path.mkdir(
        parents=True,
        exist_ok=True,
    )

    (session_path / "resume_index").mkdir()

    (session_path / "jd_index").mkdir()

    return session_id


def get_session_path(
    session_id: str,
) -> Path:

    return BASE_STORAGE / session_id


def get_resume_path(
    session_id: str,
) -> Path:

    return (
        get_session_path(session_id)
        / "resume.pdf"
    )


def get_jd_path(
    session_id: str,
) -> Path:

    return (
        get_session_path(session_id)
        / "jd.txt"
    )


def get_resume_index_path(
    session_id: str,
) -> Path:

    return (
        get_session_path(session_id)
        / "resume_index"
    )


def get_jd_index_path(
    session_id: str,
) -> Path:

    return (
        get_session_path(session_id)
        / "jd_index"
    )


def get_state_path(
    session_id: str,
) -> Path:

    return (
        get_session_path(session_id)
        / "interview_state.json"
    )


def get_report_path(
    session_id: str,
) -> Path:

    return (
        get_session_path(session_id)
        / "report.json"
    )