from datasets import load_dataset

def main():
    print("Downloading HumanEval dataset...")

    dataset = load_dataset("openai/openai_humaneval")

    print("\nDataset structure:")
    print(dataset)

    print("\nColumns:")
    print(dataset["test"].column_names)

    print("\nNumber of tasks:")
    print(len(dataset["test"]))

    print("\nExample task:\n")

    sample = dataset["test"][0]

    for key, value in sample.items():
        print(f"\n--- {key} ---\n{str(value)[:500]}")

if __name__ == "__main__":
    main()