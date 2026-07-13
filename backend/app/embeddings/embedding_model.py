from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:
    """
    Loads and provides the embedding model.
    """

    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5",
            model_kwargs={
            "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            }
        )

    def get_embeddings(self):
        return self.embeddings