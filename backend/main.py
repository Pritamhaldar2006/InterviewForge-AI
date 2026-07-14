from pathlib import Path

from app.config.llm import get_llm
from app.loaders.resume_loader import ResumeLoader
from app.splitters.resume_splitter import ResumeSplitter
from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.faiss_manager import FAISSManager
from app.chains.rag_chain import build_rag_chain
from app.retrievers.resume_retriever import get_retriever, load_vectorstore
 


def main():
    
    llm = get_llm()

    embeddings = EmbeddingModel().get_embeddings()

    vectorstore = load_vectorstore(
        "faiss_index",
        embeddings,
    )

    retriever = get_retriever(
        vectorstore,
        k=3,
    )

    rag_chain = build_rag_chain(
        llm,
        retriever,
    )

    question = "Does the candidate know fastapi.answer is yes or no"

    answer = rag_chain.invoke(question)

    print("\nAnswer:\n")

    print(answer)

if __name__ == "__main__":
    main()