from os import getenv
from dotenv import load_dotenv
from chat_loop import calculate, parse_and_calculate

import openai

load_dotenv()
openai.api_key = getenv("OPENAI_API_KEY")

messages = [
    {
        "role": "system",
        "content": """
        You are ChatGPT, a large language model trained by OpenAI. However, you specialize in mathematics using LaTeX.

        ChatGPT, in this conversation, when you want to display a mathematical expression in LaTeX, please use double dollar signs $$ and $$ to surround it.
        For example, to display the expression '2 + 2', write $$2 + 2$$.

        When you want a mathematical expression to be computed, use double curly brackets {{ and }} as placeholders for the calculation's result.
        Do not attempt to compute the result yourself, and do not provide the answer in your response.
        For instance, if you want to display the computation of '2 + 2', write $$2 + 2$$ = {{2 + 2}}, and nothing else after that.
        The system will interpret any text within double curly brackets as a LaTeX mathematical expression to be solved and spliced into the final output.

        Please do not provide the answer in any form in your response.
        """,
    }
]

def chat_loop():
    while True:
        message = input("You: ").strip()
        messages.append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
            model=getenv("OPENAI_MODEL"), messages=messages
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

        parsed_reply = parse_and_calculate(reply, calculate)

        print("ChatGPT: " + parsed_reply)

