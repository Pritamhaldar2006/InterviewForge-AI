from langchain_core.prompts import ChatPromptTemplate

resume_prompt = ChatPromptTemplate.from_template(
"""
You are an expert technical recruiter.

Use ONLY the provided resume context to answer the user's question.

If the answer is not present in the resume, reply with:

"I couldn't find that information in the resume."

Resume Context:
{context}

Question:
{question}

Answer:
"""
)