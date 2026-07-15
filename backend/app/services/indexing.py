from app.splitters.resume_splitter import split_documents
from app.vectorstore.faiss_manager import (
    create_vectorstore,
    save_vectorstore,
)


def create_index(
    documents,
    embeddings,
    save_path,
):
    """
    Create and save a FAISS index.
    """

    chunks = split_documents(documents)

    vectorstore = create_vectorstore(
        chunks,
        embeddings,
    )

    save_vectorstore(
        vectorstore,
        save_path,
    )

    return vectorstore