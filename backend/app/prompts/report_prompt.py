from langchain_core.prompts import ChatPromptTemplate

report_prompt = ChatPromptTemplate.from_template(
"""
You are a senior technical interviewer.

Below is the complete interview history.

Interview History

{history}

Generate a professional interview report.

Return:

- Overall Score (0-10)
- Strengths
- Weaknesses
- Summary
- Recommendation
- Hiring Decision

Hiring Decision must be one of:

- Strong Hire
- Hire
- Borderline
- No Hire

Return only structured output.
"""
)