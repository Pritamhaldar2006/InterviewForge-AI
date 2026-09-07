from app.models.interview_state import InterviewState

from app.services.analysis_services import (
    compare_resume_and_jd,
)

from app.services.interview_plan_service import (
    generate_interview_plan,
)

from app.services.session_service import (
    get_resume_index_path,
    get_jd_index_path,
)

from app.services.state_service import (
    save_interview_state,
)


def start_interview(
    session_id: str,
):

    # ---------------------------------------------
    # Get session indexes
    # ---------------------------------------------

    resume_index_path = get_resume_index_path(
        session_id
    )

    jd_index_path = get_jd_index_path(
        session_id
    )

    # ---------------------------------------------
    # Analyze resume vs JD
    # ---------------------------------------------

    analysis = compare_resume_and_jd(
        str(resume_index_path),
        str(jd_index_path),
    )

    # ---------------------------------------------
    # Generate interview plan
    # ---------------------------------------------

    plan = generate_interview_plan(
        analysis
    )

    # ---------------------------------------------
    # Create interview state
    # ---------------------------------------------

    state = InterviewState(
        analysis=analysis,
        plan=plan,
    )

    # ---------------------------------------------
    # Persist state
    # ---------------------------------------------

    save_interview_state(
        session_id,
        state,
    )

    return state