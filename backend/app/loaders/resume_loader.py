from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class ResumeLoader:
    """
    Loads a resume PDF and returns LangChain Document objects.
    """

    def __init__(self, resume_path: str):
        self.resume_path = Path(resume_path)

    def load(self) -> list[Document]:
        """
        Load the resume and return a list of LangChain Documents.
        """

        if not self.resume_path.exists():
            raise FileNotFoundError(
                f"Resume not found: {self.resume_path}"
            )

        loader = PyPDFLoader(str(self.resume_path))

        documents = loader.load()

        return documents