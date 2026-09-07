from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

_llm = None


def get_llm():

    global _llm

    if _llm is None:

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found.")

        _llm = ChatGroq(
            api_key=api_key,
            model="qwen/qwen3.8-27b",
            temperature=0.3,
            max_tokens=800
        )

    return _llm