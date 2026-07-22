from app.models.questions import InterviewQuestion
from app.prompts.question_prompt import question_prompt


def build_question_chain(llm):

    structured_llm = llm.with_structured_output(
        InterviewQuestion
    )

    return (
        question_prompt
        | structured_llm
    )