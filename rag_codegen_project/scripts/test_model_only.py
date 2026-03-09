from app.generator import get_client
from app.config import settings

def main():
    client = get_client()

    response = client.chat.completions.create(
        model=settings.gen_model,
        messages=[
            {"role": "system", "content": "You are a Python assistant. Reply normally."},
            {"role": "user", "content": "Write a Python function that adds two numbers."},
        ],
        temperature=0.1,
        max_tokens=300,
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()