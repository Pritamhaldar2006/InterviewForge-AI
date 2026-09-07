from app.models.interview_state import InterviewState

from app.services.session_service import (
    get_state_path,
)

from app.services.storage_service import (
    save_model,
    load_model,
)


def save_interview_state(
    session_id: str,
    state: InterviewState,
):
    save_model(
        get_state_path(session_id),
        state,
    )


def load_interview_state(
    session_id: str,
) -> InterviewState:

    return load_model(
        get_state_path(session_id),
        InterviewState,
    )