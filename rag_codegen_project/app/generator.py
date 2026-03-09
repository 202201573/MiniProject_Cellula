from openai import OpenAI
from app.config import settings
from app.prompts import SYSTEM_PROMPT


def get_client():
    if not settings.openrouter_api_key:
        raise RuntimeError("OPENROUTER_API_KEY is missing in .env")

    return OpenAI(
        base_url=settings.openrouter_base_url,
        api_key=settings.openrouter_api_key,
    )


def generate_with_context(query: str, context: str) -> str:
    client = get_client()

    user_message = f"""
Solve this Python task:

{query}

Helpful hint:
{context}

Return:
- one short explanation sentence
- one Python code block only

Do not repeat the task.
Do not repeat the hint.
""".strip()

    response = client.chat.completions.create(
        model=settings.gen_model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.0,
        max_tokens=300,
    )

    answer = response.choices[0].message.content.strip()

    if not answer:
        raise RuntimeError("Model returned an empty answer.")

    return answer


def explain_with_context(query: str, context: str) -> str:
    client = get_client()

    user_message = f"""
Answer this programming question clearly.

Question:
{query}

Helpful hint:
{context}

Return:
- a simple explanation
- short and clear
- no code unless needed
""".strip()

    response = client.chat.completions.create(
        model=settings.gen_model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.2,
        max_tokens=300,
    )

    answer = response.choices[0].message.content.strip()

    if not answer:
        raise RuntimeError("Model returned an empty explanation.")

    return answer