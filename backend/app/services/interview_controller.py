from app.models.interview_state import InterviewState
from app.models.answer_evaluation import AnswerEvaluation


def update_interview_state(
    state: InterviewState,
    evaluation: AnswerEvaluation,
):

    new_state = state.model_copy(deep=True)

    topic = new_state.plan.topics[new_state.current_topic]

    subtopic = topic.subtopics[new_state.current_subtopic]

    # ----------------------------
    # Track strong / weak subtopics
    # ----------------------------

    if evaluation.score >= 8:

        if subtopic.name not in new_state.strong_topics:
            new_state.strong_topics.append(subtopic.name)

    elif evaluation.score < 6:

        if subtopic.name not in new_state.weak_topics:
            new_state.weak_topics.append(subtopic.name)

    # ----------------------------
    # Follow-up handling
    # ----------------------------

    if (
        evaluation.follow_up_required
        and new_state.follow_up_count < new_state.max_follow_ups
    ):

        new_state.follow_up_count += 1

        return new_state

    # Reset follow-up counter
    new_state.follow_up_count = 0

    # ----------------------------
    # Move to next subtopic
    # ----------------------------

    new_state.current_subtopic += 1

    # Finished all subtopics?
    if (
        new_state.current_subtopic
        >= len(topic.subtopics)
    ):

        new_state.current_subtopic = 0

        new_state.current_topic += 1

    # Finished all topics?
    if (
        new_state.current_topic
        >= len(new_state.plan.topics)
    ):

        new_state.interview_completed = True

    return new_state