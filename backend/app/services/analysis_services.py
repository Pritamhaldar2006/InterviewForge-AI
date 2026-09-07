from app.config.llm import get_llm

from app.embeddings.embedding_model import get_embedding_model

from app.vectorstore.faiss_manager import load_vectorstore

from app.retrievers.resume_retriever import get_retriever

from app.chains.jd_match_chain import build_jd_match_chain


def format_docs(documents):

    return "\n\n".join(
        doc.page_content
        for doc in documents
    )


def compare_resume_and_jd(
    resume_index_path: str,
    jd_index_path: str,
):

    llm = get_llm()

    embeddings = get_embedding_model()

    resume_store = load_vectorstore(
    resume_index_path,
    embeddings,
)

    jd_store = load_vectorstore(
    jd_index_path,
    embeddings,
)

    resume_retriever = get_retriever(
        resume_store
    )

    jd_retriever = get_retriever(
        jd_store
    )

    resume_docs = resume_retriever.invoke(
        "Summarize the candidate."
    )

    jd_docs = jd_retriever.invoke(
        "Summarize the job description."
    )

    chain = build_jd_match_chain(
        llm
    )

    return chain.invoke(
        {
            "resume": format_docs(
                resume_docs
            ),
            "job_description": format_docs(
                jd_docs
            ),
        }
    )