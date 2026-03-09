from collections import defaultdict

_session_store = defaultdict(list)

def add_message(session_id: str, role: str, content: str):
    _session_store[session_id].append({
        "role": role,
        "content": content
    })

def get_history(session_id: str, limit: int = 6):
    return _session_store[session_id][-limit:]

def clear_history(session_id: str):
    _session_store[session_id] = []