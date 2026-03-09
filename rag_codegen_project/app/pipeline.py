from app.router import route_query
from app.retriever import retrieve_similar_tasks, format_context
from app.generator import generate_with_context, explain_with_context
from app.memory import add_message, get_history


def format_history(history: list[dict]) -> str:
    if not history:
        return "No previous conversation."

    parts = []
    for msg in history:
        parts.append(f"{msg['role'].upper()}: {msg['content']}")
    return "\n".join(parts)


def run_pipeline(query: str, session_id: str = "default"):
    add_message(session_id, "user", query)

    route = route_query(query)
    results = retrieve_similar_tasks(query, k=1)
    context = format_context(results)

    history = get_history(session_id)
    history_text = format_history(history)

    enriched_query = f"""
Conversation History:
{history_text}

Current User Query:
{query}
""".strip()

    if route["intent"] == "explain":
        answer = explain_with_context(enriched_query, context)
    else:
        answer = generate_with_context(enriched_query, context)

    add_message(session_id, "assistant", answer)

    return {
        "intent": route["intent"],
        "context": context,
        "history": history_text,
        "answer": answer,
    }