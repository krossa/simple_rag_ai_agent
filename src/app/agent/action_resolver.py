from app.agent.llm import ask_llm

def decide_action(question: str) -> str:
    prompt = f"""
    Decide what to do:

    Question: {question}

    Rules:
        - Use "search" if question is related to building an AI agent, vector databases, embeddings, llms, RAG or semantic search       
        - Use "answer" for non-technical questions, general knowledge, or if the question is not related to the topics mentioned above

Return ONLY one word: search or answer
    """

    response = ask_llm(prompt)

    return "search" if "search" in response.lower() else "answer"