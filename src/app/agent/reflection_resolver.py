from app.agent.llm import ask_llm


def reflect(question: str, answer: str, context: list[str]) -> str:
    prompt = f"""
    Evaluate the answer.

    Question: {question}
    Answer: {answer}
    Context: {context}

    Is the answer correct and grounded in the context?

    Respond:
    - GOOD
    - BAD: <reason>
    """

    return ask_llm(prompt)