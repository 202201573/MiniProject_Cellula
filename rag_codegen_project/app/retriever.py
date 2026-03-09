from app.vectordb import get_task_store


def retrieve_similar_tasks(query: str, k: int = 1):
    store = get_task_store()
    results = store.similarity_search_with_score(query, k=k)

    output = []
    for doc, score in results:
        output.append({
            "score": float(score),
            "task_id": doc.metadata.get("task_id"),
            "entry_point": doc.metadata.get("entry_point"),
            "content": doc.page_content,
        })

    return output


def extract_function_signature(text: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("def "):
            return line
    return ""


def format_context(results: list[dict]) -> str:
    if not results:
        return ""

    item = results[0]
    signature = extract_function_signature(item["content"])

    return f"""Relevant function name: {item['entry_point']}
Relevant function signature: {signature}
Similarity: {item['score']:.4f}"""