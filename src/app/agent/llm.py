from openai import OpenAI

_client = OpenAI()


def ask_llm(prompt: str) -> str:
    response = _client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content