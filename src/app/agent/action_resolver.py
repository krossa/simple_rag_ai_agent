def decide_action(question: str) -> str:
    prompt = f"""
Decide what to do:

Question: {question}

Options:
- search (if needs external knowledge)
- answer (if simple)

Return only one word.
"""

    response = llm(prompt)

    return "search" if "search" in response.lower() else "answer"