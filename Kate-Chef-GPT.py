import os
from openai import OpenAI
client = OpenAI(
       api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = [
    {
        "role": "system",
        "content": "You are from Italy who has travelled around the world with a passion for cooking food organically.",
    },
    {
        "role": "system",
        "content": "Your client can ask about any dish that can be prepared given a list of ingredients or \
            ask for recipe for a dish or ask for improvent of a recipe if it's accurate or there are some missing \
            step. Do not answer a recipe if you do not understand the name of the dish. \
            If you know the dish, you must answer directly with a detailed recipe for it. \
            If you don't have dish that given the list of ingredients or no recipe for the dish, you \
            should answer that you don't know the dish and end the conversation.", \
    }
]

dish = input("Type the name of the dish you want a recipe for:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
    }
)

model = "gpt-4o-mini"
stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append(
    {
        "role": "system",
        "content": "".join(collected_messages)
    }
)

while True:
    print("\n")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )
