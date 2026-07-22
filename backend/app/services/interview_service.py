from app.services.analysis_services import (
    compare_resume_and_jd,
)
from app.models.interview_state import InterviewState
from app.services.interview_plan_service import generate_interview_plan


def start_interview():

    analysis = compare_resume_and_jd()

    plan = generate_interview_plan()

    state = InterviewState(
        analysis=analysis,
        plan=plan,
    )

    return state