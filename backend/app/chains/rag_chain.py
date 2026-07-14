from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from app.prompts.resume_prompt import resume_prompt


def format_docs(documents):
    """
    Convert retrieved Documents into a single string.
    """

    return "\n\n".join(
        doc.page_content
        for doc in documents
    )


def build_rag_chain(llm, retriever):
    """
    Build the complete RAG chain.
    """

    chain = (

        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }

        | resume_prompt

        | llm

        | StrOutputParser()

    )

    return chain