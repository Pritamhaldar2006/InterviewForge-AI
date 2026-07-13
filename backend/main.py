from pathlib import Path

from app.config.llm import get_llm
from app.loaders.resume_loader import ResumeLoader
from app.splitters.resume_splitter import ResumeSplitter


def main():
    resume_path = Path(__file__).resolve().parent / "data" / "resumes" / "ResumeSamrat2025.pdf"
    loader = ResumeLoader(str(resume_path))
    documents = loader.load()

    print(f"Pages Loaded: {len(documents)}")

    print("\nFirst Page:\n")

    print(documents[0].page_content)

    splitter = ResumeSplitter()

    chunks = splitter.split(documents)

    print(f"\nTotal Chunks: {len(chunks)}\n")

    for i, chunk in enumerate(chunks):

        print("=" * 60)
        print(f"Chunk {i+1}")
        print("=" * 60)

        print(chunk.page_content)

        print()
if __name__ == "__main__":
    main()