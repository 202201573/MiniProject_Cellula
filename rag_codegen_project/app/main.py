from fastapi import FastAPI
from pydantic import BaseModel
from app.pipeline import run_pipeline
from app.memory import clear_history

app = FastAPI(title="RAG Code Assistant")


class ChatRequest(BaseModel):
    session_id: str
    query: str


class ChatResponse(BaseModel):
    intent: str
    context: str
    history: str
    answer: str


@app.get("/")
def root():
    return {"message": "RAG Code Assistant is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    result = run_pipeline(req.query, session_id=req.session_id)
    return ChatResponse(**result)


@app.post("/clear_memory")
def clear(req: ChatRequest):
    clear_history(req.session_id)
    return {"message": f"Memory cleared for session '{req.session_id}'"}