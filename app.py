from dotenv import load_dotenv
from openai import OpenAI
import os
from importlib import import_module

load_dotenv()

prompt_creator = os.getenv('PROMPT_CREATOR', 'sys')
prompts = import_module(f'prompts.{prompt_creator}')
from utils import system_message, user_message


client = OpenAI()

messages = [
    system_message(prompts.CHEF_DESCRIPTION),
    system_message(prompts.RECIPE_INSTRUCTIONS),
]

dish = input("Your question：\n")
messages.append(
    user_message(prompts.USER_INSTRUCTIONS.format(dish=dish))
)

model = os.getenv('MODEL', 'gpt-4o-mini')

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
