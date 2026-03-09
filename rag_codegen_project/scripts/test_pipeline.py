from app.pipeline import run_pipeline


def main():
    queries = [
        "Explain how to check whether any two numbers in a list are closer than a threshold.",
        "Write a Python function that returns True if any two numbers in a list are closer than a threshold, otherwise False."
    ]

    for query in queries:
        print("\n" + "=" * 100)
        print("USER QUERY:")
        print(query)

        result = run_pipeline(query)

        print("\nROUTE:")
        print(result["intent"])
        print(result["reason"])

        print("\nCONTEXT:")
        print(result["context"])

        print("\nANSWER:")
        print(result["answer"])


if __name__ == "__main__":
    main()