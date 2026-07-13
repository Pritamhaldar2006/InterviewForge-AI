from pathlib import Path

from app.config.llm import get_llm
from app.loaders.resume_loader import ResumeLoader
from app.splitters.resume_splitter import ResumeSplitter
from app.embeddings.embedding_model import EmbeddingModel
from app.vectorstore.faiss_manager import FAISSManager

def main():
     # Load resume
    resume_path = Path(__file__).resolve().parent / "data" / "resumes" / "ResumeSamrat2025.pdf"
    loader = ResumeLoader(str(resume_path))
    documents = loader.load()

    # Split into chunks
    splitter = ResumeSplitter()
    chunks = splitter.split(documents)

    print(f"Chunks created: {len(chunks)}")

    # Load embedding model
    embeddings = EmbeddingModel().get_embeddings()

    # Create vector store
    manager = FAISSManager(embeddings)

    vectorstore = manager.create_vectorstore(chunks)

    # Save locally
    manager.save_vectorstore(
        vectorstore,
        "faiss_index"
    )

    print("\nFAISS index created successfully!")
    print("Saved in: faiss_index/")
if __name__ == "__main__":
    main()