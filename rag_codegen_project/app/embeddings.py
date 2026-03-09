from langchain_huggingface import HuggingFaceEmbeddings
from app.config import settings

_embedding_instance = None

def get_embedding_function():
    global _embedding_instance

    if _embedding_instance is None:
        _embedding_instance = HuggingFaceEmbeddings(
            model_name=settings.embed_model
        )

    return _embedding_instance