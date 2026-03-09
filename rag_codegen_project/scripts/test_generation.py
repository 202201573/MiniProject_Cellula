from app.retriever import retrieve_similar_tasks, format_context
from app.generator import generate_with_context


def main():
    query = "Write a Python function that returns True if any two numbers in a list are closer than a threshold, otherwise False."

    print("\nUser Query:\n")
    print(query)
    print("\n" + "=" * 80)

    results = retrieve_similar_tasks(query, k=1)
    context = format_context(results)

    print("\nRetrieved Context:\n")
    print(context)
    print("\n" + "=" * 80)

    print("\nGenerating answer from model...\n")
    answer = generate_with_context(query, context)

    print("\nModel Answer:\n")
    print(answer)


if __name__ == "__main__":
    main()