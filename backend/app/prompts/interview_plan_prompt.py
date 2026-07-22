from langchain_core.prompts import ChatPromptTemplate

interview_plan_prompt = ChatPromptTemplate.from_template(
"""
You are an experienced technical interviewer.

Based on the resume analysis below, create an interview plan.

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

Instructions:

1. Cover both strengths and weaknesses.
2. Ask more questions on weak areas.
3. Difficulty should be Beginner, Intermediate, or Advanced.
4. Return only the interview plan.
"""
)