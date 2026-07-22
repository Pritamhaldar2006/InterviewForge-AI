from app.config.llm import get_llm

from app.chains.question_chain import build_question_chain

from app.models.interview_state import InterviewState


def generate_question(
    state: InterviewState,
):

    topic = state.plan.topics[state.current_topic]

    llm = get_llm()

    chain = build_question_chain(llm)

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

    return question