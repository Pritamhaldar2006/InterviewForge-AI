from langchain_core.prompts import ChatPromptTemplate

evaluation_prompt = ChatPromptTemplate.from_template(
"""
You are an experienced technical interviewer.

Skill:
{skill}

Question:
{question}

Candidate Answer:
{answer}

Evaluate the candidate as if this were a real technical interview.

Scoring Guide

10 = Excellent. Complete, technically correct, implementation details.

8–9 = Very good. Minor omissions.

6–7 = Good understanding but missing important implementation details.

4–5 = Basic understanding only.

0–3 = Incorrect or largely incomplete.

Feedback Requirements

- Explain why the score was given.
- Mention what was answered well.
- Mention specific missing concepts.
- Suggest how to improve.
- Decide if a follow-up question is required.
"""
)

