from pathlib import Path

from langchain_core.documents import Document


def load_text(path: str):
    """
    Load a plain text file as a LangChain Document.
    """

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"{path} not found.")

    text = file_path.read_text(encoding="utf-8")

    return [
        Document(
            page_content=text,
            metadata={
                "source": str(file_path)
            },
        )
    ]