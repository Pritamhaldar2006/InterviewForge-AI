from pathlib import Path

from app.config.llm import get_llm
from app.loaders.resume_loader import ResumeLoader
from app.splitters.resume_splitter import ResumeSplitter
from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.faiss_manager import FAISSManager
from app.chains.rag_chain import build_rag_chain
from app.chains.jd_match_chain import build_jd_match_chain
from app.retrievers.resume_retriever import get_retriever, load_vectorstore
 
def format_docs(documents):
    """
    Convert LangChain Documents into a single string.
    """
    return "\n\n".join(
        doc.page_content
        for doc in documents
    )

def main():
    
    llm = get_llm()

    embeddings = EmbeddingModel().get_embeddings()

    resume_vectorstore = load_vectorstore(
        "faiss_index/resume",
        embeddings,
    )

    resume_retriever = get_retriever(
        resume_vectorstore,
        k=3,
    )

    # -------------------------------
    # Load Job Description Vector Store
    # -------------------------------

    jd_vectorstore = load_vectorstore(
        "faiss_index/job_description",
        embeddings,
    )

    jd_retriever = get_retriever(
        jd_vectorstore,
        k=3,
    )


    # -------------------------------
    # Retrieve Resume Context
    # -------------------------------

    resume_docs = resume_retriever.invoke(
        "Summarize the candidate's skills, projects, and experience."
    )

    # -------------------------------
    # Retrieve JD Context
    # -------------------------------

    jd_docs = jd_retriever.invoke(
        "Summarize the required skills, responsibilities, and qualifications."
    )

    # -------------------------------
    # Convert Documents to Text
    # -------------------------------

    resume_context = format_docs(resume_docs)

    jd_context = format_docs(jd_docs)

    # -------------------------------
    # Build Comparison Chain
    # -------------------------------

    match_chain = build_jd_match_chain(llm)

    # -------------------------------
    # Compare Resume and JD
    # -------------------------------

    analysis = match_chain.invoke(
        {
            "resume": resume_context,
            "job_description": jd_context,
        }
    )

    # -------------------------------
    # Print Result
    # -------------------------------

    print("\n" + "=" * 80)
    print(" Resume vs Job Description Analysis ")
    print("=" * 80 + "\n")

    print(analysis)



if __name__ == "__main__":
    main()