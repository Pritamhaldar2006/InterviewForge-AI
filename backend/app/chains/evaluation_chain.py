from app.models.answer_evaluation import AnswerEvaluation
from app.prompts.evaluation_prompt import evaluation_prompt


def build_evaluation_chain(llm):

    structured_llm = llm.with_structured_output(
        AnswerEvaluation
    )

    return (
        evaluation_prompt
        | structured_llm
    )