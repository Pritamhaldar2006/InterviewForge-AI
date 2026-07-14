from langchain_community.vectorstores import FAISS


def load_vectorstore(path: str, embeddings):
    """
    Load an existing FAISS index.
    """

    return FAISS.load_local(
        folder_path=path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True,
    )


def get_retriever(vectorstore: FAISS, k: int = 3):
    """
    Create a retriever from the FAISS vector store.
    """

    return vectorstore.as_retriever(
        search_kwargs={
            "k": k
        }
    )