from pathlib import Path

from langchain_core.documents import Document

from app.embeddings.embedding_model import get_embedding_model

from app.splitters.resume_splitter import split_documents

from app.vectorstore.faiss_manager import (
    create_vectorstore,
    save_vectorstore,
)


def build_vectorstore(
    documents: list[Document],
    save_path: str,
    chunk_size: int = 500,
    chunk_overlap: int = 100,
):
    embeddings = get_embedding_model()

    chunks = split_documents(documents,chunk_overlap=chunk_overlap,chunk_size=chunk_size)

    vectorstore = create_vectorstore(
        chunks,
        embeddings,
    )

    Path(save_path).mkdir(
        parents=True,
        exist_ok=True,
    )

    save_vectorstore(
        vectorstore,
        save_path,
    )

    return save_path