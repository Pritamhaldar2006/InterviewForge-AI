from pathlib import Path

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
)

from app.services.session_service import (
    get_session_path,
    get_resume_path,
)

from app.services.session_file_service import (
    save_resume,
)


router = APIRouter(
    prefix="/sessions",
    tags=["Sessions"],
)


@router.post("")
def create_interview_session():

    from app.services.session_service import (
        create_session,
    )

    session_id = create_session()

    return {
        "session_id": session_id
    }


@router.post("/{session_id}/resume")
async def upload_resume(
    session_id: str,
    file: UploadFile = File(...),
):

    # ---------------------------------------------
    # Check session
    # ---------------------------------------------

    session_path = get_session_path(
        session_id
    )

    if not session_path.exists():

        raise HTTPException(
            status_code=404,
            detail="Session not found.",
        )

    # ---------------------------------------------
    # Validate file type
    # ---------------------------------------------

    if file.content_type != "application/pdf":

        raise HTTPException(
            status_code=400,
            detail="Only PDF resumes are allowed.",
        )

    # ---------------------------------------------
    # Save file temporarily
    # ---------------------------------------------

    temp_path = (
        session_path / "upload.tmp"
    )

    try:

        with open(
            temp_path,
            "wb",
        ) as buffer:

            while chunk := await file.read(
                1024 * 1024
            ):

                buffer.write(chunk)

        # -----------------------------------------
        # Save using service
        # -----------------------------------------

        save_resume(
            session_id,
            str(temp_path),
        )

    finally:

        if temp_path.exists():
            temp_path.unlink()

    return {
        "message": "Resume uploaded successfully.",
        "session_id": session_id,
        "filename": file.filename,
        "path": str(
            get_resume_path(session_id)
        ),
    }