from app.agent.llm import ask_llm

def generate_answer(question: str, chunks: list[str]=None) -> str:
    if chunks is None:
        chunks = []
    context = "\n\n".join(chunks)

    prompt = f"""
    You are a helpful assistant.

    First use ONLY the context below to answer the question.
    If the answer is not in the context, then reply that answer was not in the context.
    And give your best answer.".

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    return ask_llm(prompt)