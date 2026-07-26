from app.config.llm import get_llm

from app.chains.evaluation_chain import build_evaluation_chain

from app.models.interview_state import InterviewState


def evaluate_answer(
    state: InterviewState,
    answer: str,
):

    topic = state.plan.topics[state.current_topic]

    subtopic = topic.subtopics[state.current_subtopic]

    last_question = state.history[-1]

    llm = get_llm()

    chain = build_evaluation_chain(llm)

    evaluation = chain.invoke(
        {
            "skill": topic.skill,
            "question": last_question.question,
            "answer": answer,
        }
    )

    new_state = state.model_copy(deep=True)

    history = new_state.history[-1]

    history.answer = answer
    history.score = evaluation.score
    history.feedback = evaluation.feedback
    history.strengths = evaluation.strengths
    history.improvements = evaluation.improvements
    history.follow_up = evaluation.follow_up_required

    # Track strengths by subtopic
    if evaluation.score >= 8:

        if subtopic.name not in new_state.strong_topics:
            new_state.strong_topics.append(subtopic.name)

    # Track weaknesses by subtopic
    elif evaluation.score < 6:

        if subtopic.name not in new_state.weak_topics:
            new_state.weak_topics.append(subtopic.name)

    # Adaptive difficulty
    if evaluation.score >= 9:
        new_state.current_difficulty = "Advanced"

    elif evaluation.score >= 6:
        new_state.current_difficulty = "Intermediate"

    else:
        new_state.current_difficulty = "Beginner"

    return new_state, evaluation