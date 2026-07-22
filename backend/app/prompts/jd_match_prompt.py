from langchain_core.prompts import ChatPromptTemplate

jd_match_prompt = ChatPromptTemplate.from_template(
"""
You are an experienced technical recruiter.

Compare the candidate's resume with the job description.

Resume:

{resume}

Job Description:

{job_description}

Analyze:

- Matching Skills
- Missing Skills
- Candidate Strengths
- Candidate Weaknesses
- Overall Summary

Return accurate structured information.
"""
)