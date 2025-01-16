#Create a human-like response to a prompt

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "새해 인사말을 작성해줘."
        }
    ]
)

print(completion.choices[0].message.content)
