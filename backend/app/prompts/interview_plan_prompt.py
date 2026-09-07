from langchain_core.prompts import ChatPromptTemplate

interview_plan_prompt = ChatPromptTemplate.from_template(
"""
You are a senior software engineering interviewer.

Your task is to design a structured interview plan.

Resume Analysis

Matching Skills:
{matching_skills}

Missing Skills:
{missing_skills}

Strengths:
{strengths}

Weaknesses:
{weaknesses}

Summary:
{summary}

Instructions
Instructions

1. Choose at most {max_questions} technical skills.
2. Generate ONLY ONE interview question for each skill.
3. Prioritise skills that are important for the job description.
4. Cover both strengths and weaknesses.
5. Focus on theory and conceptual questions.
6. Return only structured output.

"""
)


# 1. Choose the {max_questions} most important technical skills.
# 2. Prioritize missing skills and weak areas.
# 3. Also assess important matching skills.
# 4. For every skill generate 3-5 unique subtopics.
# 5. Subtopics must not repeat.
# 6. Order subtopics from easier to harder.
# 7. Focus on implementation and practical knowledge.
# 8. Every subtopic should represent exactly one interview question.
# 9. Return only structured output.