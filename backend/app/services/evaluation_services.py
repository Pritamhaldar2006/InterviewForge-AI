from app.config.llm import get_llm

from app.chains.evaluation_chain import (
    build_evaluation_chain,
)

from app.models.interview_state import (
    InterviewState,
)


def evaluate_answer(
    state: InterviewState,
    answer: str,
):

    topic = state.plan.topics[
        state.current_topic
    ]

    last_question = state.history[-1]

    llm = get_llm()

    chain = build_evaluation_chain(
        llm
    )

    evaluation = chain.invoke(
        {
            "skill": topic.skill,
            "question": last_question.question,
            "answer": answer,
        }
    )

    new_state = state.model_copy(deep=True)

    new_state.history[-1].answer = answer
    new_state.history[-1].score = evaluation.score
    new_state.history[-1].feedback = evaluation.feedback

    if evaluation.score >= 8:

        if topic.skill not in new_state.strong_topics:
            new_state.strong_topics.append(
                topic.skill
            )

    else:

        if topic.skill not in new_state.weak_topics:
            new_state.weak_topics.append(
                topic.skill
            )

    return new_state, evaluation