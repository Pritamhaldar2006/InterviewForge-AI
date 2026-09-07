from app.config.llm import get_llm

from app.chains.question_chain import (
    build_question_chain,
)

from app.models.interview_state import (
    QuestionAnswer,
)

from app.services.state_service import (
    load_interview_state,
    save_interview_state,
)


def generate_question(
    session_id: str,
):

    state = load_interview_state(
        session_id
    )

    # --------------------------------------------------
    # Check whether interview is already completed
    # --------------------------------------------------

    if state.interview_completed:

        raise ValueError(
            "Interview is already completed."
        )

    # --------------------------------------------------
    # Get current topic
    # --------------------------------------------------

    topic = state.plan.topics[
        state.current_topic
    ]

    # --------------------------------------------------
    # Generate question
    # --------------------------------------------------

    llm = get_llm()

    chain = build_question_chain(
        llm
    )

    question = chain.invoke(
        {
            "skill": topic.skill,
            "difficulty": topic.difficulty,
            "history": [
                item.question
                for item in state.history
            ],
        }
    )

    # --------------------------------------------------
    # Add question to history
    # --------------------------------------------------

    state.history.append(
        QuestionAnswer(
            skill=topic.skill,
            difficulty=topic.difficulty,
            question=question.question,
        )
    )

    # --------------------------------------------------
    # Save updated state
    # --------------------------------------------------

    save_interview_state(
        session_id,
        state,
    )

    return question