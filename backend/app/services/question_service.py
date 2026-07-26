from app.config.llm import get_llm

from app.chains.question_chain import build_question_chain

from app.models.interview_state import (
    InterviewState,
    QuestionAnswer,
)


def generate_question(
    state: InterviewState,
):
    topic = state.plan.topics[state.current_topic]

    subtopic = topic.subtopics[state.current_subtopic]

    llm = get_llm()

    chain = build_question_chain(llm)

    question = chain.invoke(
    {
        "skill": topic.skill,
        "subtopic": subtopic.name,
        "difficulty": subtopic.difficulty,
        "history": [
            {
                "question": item.question,
                "subtopic": item.subtopic,
                "score": item.score,
            }
            for item in state.history
        ],
        "strengths": state.strong_topics,
        "weaknesses": state.weak_topics,
        "follow_up": state.follow_up_count > 0,
    }
)

    new_state = state.model_copy(deep=True)

    new_state.history.append(
        QuestionAnswer(
            skill=topic.skill,
            subtopic=subtopic.name,
            difficulty=subtopic.difficulty,
            question=question.question,
        )
    )

    return new_state, question