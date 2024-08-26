import os
from openai import OpenAI
client = OpenAI(
       api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = [
    {
        "role": "system",
        "content": "You are very positive and very knowledgeable of Pre-Hispanic food.",
    }
]

messages.append(
    {
        "role": "system",
        "content": "Given a list of ingredients, Your client will want to know of any dishes that can be prepared with the ingredients. \
                    You should return a maximum of 3 dishes if you recognize the ingredients. \
                    You should return only the name of the recipe  \
                    Do not respond if you don't recognize atleast one of the ingredients",
    }
)

messages.append(
    {
        "role": "system",
        "content": "Your client will want a response for the recipe of any dish you specify \
                    Do not respond, if you have no knowledge of the recipe",
    }
)

messages.append(
    {
        "role": "system",
        "content": "Analyze the recipe sent and suggest improvement or mention what is wrong with recipe",
    }
)

dish = input("Ask your question regarding the ingredients or recipe or improvements?:\n")
messages.append(
    {
        "role": "user",
        "content": f"{dish}"
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