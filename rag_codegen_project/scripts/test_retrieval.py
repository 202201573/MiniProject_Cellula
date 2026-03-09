from app.retriever import retrieve_similar_tasks


def main():
    query = "Write a Python function to check whether any two numbers in a list are closer than a threshold"

    print(f"\nQuery:\n{query}\n")
    print("=" * 80)

    results = retrieve_similar_tasks(query, k=3)

    for i, item in enumerate(results, start=1):
        print(f"\nResult #{i}")
        print(f"Score      : {item['score']}")
        print(f"Task ID    : {item['task_id']}")
        print(f"Entry Point: {item['entry_point']}")
        print("\nContent:")
        print(item["content"])
        print("-" * 80)


if __name__ == "__main__":
    main()