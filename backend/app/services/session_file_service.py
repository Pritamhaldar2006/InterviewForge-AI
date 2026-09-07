from pathlib import Path
import shutil

from app.services.session_service import (
    get_resume_path,
    get_jd_path,
)


def save_resume(
    session_id: str,
    source_path: str,
):
    source = Path(source_path)

    if not source.exists():
        raise FileNotFoundError(
            f"Resume not found: {source}"
        )

    destination = get_resume_path(
        session_id
    )

    shutil.copy2(
        source,
        destination,
    )

    return destination


def save_jd(
    session_id: str,
    source_path: str,
):
    source = Path(source_path)

    if not source.exists():
        raise FileNotFoundError(
            f"JD not found: {source}"
        )

    destination = get_jd_path(
        session_id
    )

    shutil.copy2(
        source,
        destination,
    )

    return destination