from unittest import result

from app.services.vector_store import query_rag
from app.agent.agent import run_agent

def ask_question():
    question = input("Ask your question: ").strip()

    result = run_agent(question)
    
    print("\nAction:", result["action"])
    print("Reflection:", result["reflection"])
    print("\nAnswer:\n", result["answer"])
    