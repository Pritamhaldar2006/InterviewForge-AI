from langchain_core.output_parsers import StrOutputParser

from app.prompts.jd_match_prompt import jd_match_prompt


def format_docs(documents):
    return "\n\n".join(
        doc.page_content
        for doc in documents
    )


def build_jd_match_chain(llm):
    """
    Compare resume and job description.
    """

    chain = (

        jd_match_prompt

        | llm

        | StrOutputParser()

    )

    return chain