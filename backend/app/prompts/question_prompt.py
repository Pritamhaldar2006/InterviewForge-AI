from langchain_core.prompts import ChatPromptTemplate

question_prompt = ChatPromptTemplate.from_template(
"""
You are an experienced technical interviewer.

Current Skill

{skill}

Difficulty

{difficulty}

Previous Questions

{history}

Generate ONE interview question.

Rules

- Do not repeat previous questions.
- Ask only one question.
- Do not provide the answer.
- Keep the question concise.
"""
)