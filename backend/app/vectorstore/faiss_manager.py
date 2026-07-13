from pathlib import Path

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS


class FAISSManager:
    """
    Creates, saves, loads, and provides access to the FAISS vector store.
    """

    def __init__(self, embeddings):
        self.embeddings = embeddings

    def create_vectorstore(
        self,
        documents: list[Document]
    ) -> FAISS:
        """
        Create a FAISS vector store from documents.
        """

        vectorstore = FAISS.from_documents(
            documents=documents,
            embedding=self.embeddings
        )

        return vectorstore

    def save_vectorstore(
        self,
        vectorstore: FAISS,
        save_path: str
    ) -> None:
        """
        Save the FAISS index locally.
        """

        vectorstore.save_local(save_path)

    def load_vectorstore(
        self,
        save_path: str
    ) -> FAISS:
        """
        Load an existing FAISS index.
        """

        if not Path(save_path).exists():
            raise FileNotFoundError(
                f"Vector store not found at {save_path}"
            )

        vectorstore = FAISS.load_local(
            folder_path=save_path,
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True
        )

        return vectorstore