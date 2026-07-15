from pathlib import Path

from langchain_community.vectorstores import FAISS


def create_vectorstore(documents, embeddings):
    return FAISS.from_documents(
        documents=documents,
        embedding=embeddings,
    )


def save_vectorstore(vectorstore, save_path):
    vectorstore.save_local(save_path)


def load_vectorstore(save_path, embeddings):

    if not Path(save_path).exists():
        raise FileNotFoundError(
            f"{save_path} does not exist."
        )

    return FAISS.load_local(
        folder_path=save_path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True,
    )