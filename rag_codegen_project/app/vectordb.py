from langchain_chroma import Chroma
from app.embeddings import get_embedding_function
from app.config import settings

COLLECTION_TASKS = "humaneval_tasks"
COLLECTION_LEARNED = "learned_functions"


def get_task_store():
    return Chroma(
        collection_name=COLLECTION_TASKS,
        embedding_function=get_embedding_function(),
        persist_directory=settings.chroma_dir,
    )


def get_learned_store():
    return Chroma(
        collection_name=COLLECTION_LEARNED,
        embedding_function=get_embedding_function(),
        persist_directory=settings.chroma_dir,
    )