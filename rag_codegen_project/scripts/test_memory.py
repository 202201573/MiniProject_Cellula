from app.pipeline import run_pipeline


def main():
    session_id = "user_1"

    queries = [
        "Write a Python function to check whether any two numbers in a list are closer than a threshold.",
        "Now explain how that function works.",
        "Make the explanation simpler."
    ]

    for q in queries:
        print("\n" + "=" * 100)
        print("USER QUERY:")
        print(q)

        result = run_pipeline(q, session_id=session_id)

        print("\nINTENT:")
        print(result["intent"])

        print("\nHISTORY:")
        print(result["history"])

        print("\nANSWER:")
        print(result["answer"])


if __name__ == "__main__":
    main()