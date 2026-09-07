from app.config.llm import get_llm

from app.chains.report_chain import (
    build_report_chain,
)

from app.models.interview_state import (
    InterviewState,
)


def generate_report(
    state: InterviewState,
):

    llm = get_llm()

    chain = build_report_chain(llm)

    report = chain.invoke(
        {
            "history": state.history,
        }
    )

    return report