import os
import requests
import streamlit as st

st.set_page_config(
    page_title="RAG Code Assistant",
    page_icon="💬",
    layout="wide",
)

API_BASE = os.getenv("API_BASE", "http://127.0.0.1:8000")


def init_state():
    if "session_id" not in st.session_state:
        st.session_state.session_id = "demo"
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hi — I’m your RAG Code Assistant. Ask me to generate Python code or explain a programming concept.",
                "intent": "assistant",
            }
        ]


def call_chat_api(query: str, session_id: str) -> dict:
    response = requests.post(
        f"{API_BASE}/chat",
        json={"query": query, "session_id": session_id},
        timeout=120,
    )
    response.raise_for_status()
    return response.json()


def clear_memory_api(session_id: str) -> None:
    response = requests.post(
        f"{API_BASE}/clear_memory",
        json={"query": "", "session_id": session_id},
        timeout=30,
    )
    response.raise_for_status()


def reset_chat():
    try:
        clear_memory_api(st.session_state.session_id)
    except Exception:
        pass
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Memory cleared. Start a new conversation.",
            "intent": "assistant",
        }
    ]


init_state()

st.title("💬 RAG Code Assistant")
st.caption("ChatGPT-style UI for your FastAPI + Chroma + OpenRouter coding assistant")

with st.sidebar:
    st.subheader("Settings")
    st.session_state.session_id = st.text_input("Session ID", value=st.session_state.session_id)
    st.text_input("API Base URL", value=API_BASE, disabled=True)
    if st.button("Clear memory", use_container_width=True):
        reset_chat()
        st.rerun()

    st.markdown("---")
    st.markdown("**Backend check**")
    if st.button("Ping backend", use_container_width=True):
        try:
            r = requests.get(f"{API_BASE}/health", timeout=10)
            r.raise_for_status()
            st.success("Backend is running")
        except Exception as e:
            st.error(f"Backend not reachable: {e}")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("intent") and msg["role"] == "assistant":
            st.caption(f"Intent: {msg['intent']}")

prompt = st.chat_input("Ask for code or an explanation...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                data = call_chat_api(prompt, st.session_state.session_id)
                answer = data.get("answer", "No answer returned.")
                intent = data.get("intent", "unknown")
                st.markdown(answer)
                st.caption(f"Intent: {intent}")
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "intent": intent,
                    }
                )
            except Exception as e:
                err = (
                    f"I couldn't reach the backend. Make sure FastAPI is running on {API_BASE}.\n\n"
                    f"Error: {e}"
                )
                st.error(err)
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": err,
                        "intent": "error",
                    }
                )
