def run_agent(question: str):
    # 1. Reason: decide what to do
    decision = decide_action(question)

    # 2. Act: call tool
    if decision == "search":
        context = query_similar_chunks(question)
    else:
        context = []

    # 3. Generate answer
    answer = generate_answer(question, context)

    # 4. Reflect
    reflection = reflect_on_answer(question, answer, context)

    return answer, reflection