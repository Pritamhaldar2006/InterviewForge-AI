from app.models.interview_plan import InterviewPlan
from app.prompts.interview_plan_prompt import interview_plan_prompt


def build_interview_plan_chain(llm):

    structured_llm = llm.with_structured_output(
        InterviewPlan
    )

    return (
        interview_plan_prompt
        | structured_llm
    )