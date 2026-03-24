from app.agent.action_resolver import decide_action
from app.agent.question_resolver import generate_answer
from app.services.vector_store import query_rag
from app.agent.reflection_resolver import reflect as reflect_on_answer

def run_agent(question: str):
    action = decide_action(question)
    reflection = "not applicable"

    if action == "search":
        context = query_rag(question)
        answer = generate_answer(question, context["documents"])
        reflection = reflect_on_answer(question, answer, context)

    else:
        context = []
        answer = generate_answer(question)

    return {
        "answer": answer,
        "reflection":  reflection,
        "action": action
    }