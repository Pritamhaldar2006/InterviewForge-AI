from app.prompts.report_prompt import report_prompt
from app.models.interview_report import InterviewReport


def build_report_chain(llm):

    return (
        report_prompt
        | llm.with_structured_output(
            InterviewReport
        )
    )