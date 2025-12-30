import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_llm(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content