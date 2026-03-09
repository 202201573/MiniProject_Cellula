from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    openrouter_api_key: str = os.getenv("OPENROUTER_API_KEY", "")
    openrouter_base_url: str = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    gen_model: str = os.getenv("GEN_MODEL", "qwen/qwen2.5-coder-7b-instruct")
    embed_model: str = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    chroma_dir: str = os.getenv("CHROMA_DIR", "./chroma_db")
    top_k: int = int(os.getenv("TOP_K", "3"))
    max_context_chars: int = int(os.getenv("MAX_CONTEXT_CHARS", "12000"))

settings = Settings()


def validate_settings() -> None:
    errors = []

    if not settings.embed_model:
        errors.append("EMBED_MODEL is missing")

    if not settings.chroma_dir:
        errors.append("CHROMA_DIR is missing")

    if errors:
        raise RuntimeError("Config error:\n- " + "\n- ".join(errors))