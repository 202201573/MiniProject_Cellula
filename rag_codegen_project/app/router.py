def route_query(query: str) -> dict:
    q = query.lower()

    explain_words = [
        "explain",
        "what is",
        "how does",
        "why",
        "describe",
        "teach",
        "simpler",
        "simplify",
        "clarify",
    ]

    generate_words = [
        "write",
        "implement",
        "create",
        "generate",
        "build",
        "code",
        "function",
        "algorithm",
    ]

    if any(word in q for word in explain_words):
        return {
            "intent": "explain",
            "reason": "matched explanation keywords"
        }

    if any(word in q for word in generate_words):
        return {
            "intent": "generate",
            "reason": "matched generation keywords"
        }

    return {
        "intent": "explain",
        "reason": "defaulted to explain"
    }