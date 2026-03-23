from app.services.vector_store import query

def ask_question():
    question = input("Ask your question: ").strip()
    result = query(question)

    for doc, meta in zip(result["documents"], result["metadatas"]):
        print(f"[{meta['source']}] {doc}")