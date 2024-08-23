from dotenv import load_dotenv
from openai import OpenAI
from prompts import CHEF_DESCRIPTION, RECIPE_INSTRUCTIONS
from utils import system_message, user_message

load_dotenv()

client = OpenAI()

messages = [
    system_message(CHEF_DESCRIPTION),
    system_message(RECIPE_INSTRUCTIONS),
]

dish = input("請輸入：\n")
messages.append(
    user_message(dish)
)

model = "gpt-4o-mini"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
