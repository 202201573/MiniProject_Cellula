from datasets import load_dataset
from langchain_core.documents import Document
from app.vectordb import get_task_store

def make_retrieval_text(item: dict) -> str:
    prompt = item["prompt"].strip()
    entry_point = item["entry_point"].strip()

    return f"""Task ID: {item['task_id']}

Entry Point:
{entry_point}

Programming Task:
{prompt}
""".strip()


def main():
    print("Loading HumanEval dataset...")
    dataset = load_dataset("openai/openai_humaneval")
    rows = dataset["test"]

    print(f"Loaded {len(rows)} tasks")

    docs = []
    for item in rows:
        doc = Document(
            page_content=make_retrieval_text(item),
            metadata={
                "task_id": item["task_id"],
                "entry_point": item["entry_point"],
                "source": "humaneval",
                "type": "benchmark_task",
            }
        )
        docs.append(doc)

    print("Opening Chroma store...")
    store = get_task_store()

    print("Adding documents to Chroma...")
    store.add_documents(docs)

    print(f"Done. Indexed {len(docs)} documents into Chroma.")


if __name__ == "__main__":
    main()