from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_pdf(pdf_path: str) -> list[Document]:
    """
    Load a PDF file and return a list of LangChain Document objects.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        list[Document]: List of LangChain documents.
    """

    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF file not found: {pdf_path}"
        )

    loader = PyPDFLoader(str(pdf_path))

    documents = loader.load()

    return documents