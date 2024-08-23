from dotenv import load_dotenv
from openai import OpenAI
import os
from importlib import import_module

load_dotenv()

prompt_creator = os.getenv('PROMPT_CREATOR', 'sys')
prompts = import_module(f'prompts.{prompt_creator}')
from utils import system_message, user_message


client = OpenAI()

model = os.getenv('MODEL', 'gpt-4o-mini')

messages = [
    system_message(prompts.CHEF_DESCRIPTION),
    system_message(prompts.RECIPE_INSTRUCTIONS),
]


try:
    while True:
        print("\nYou can press Ctrl+C at any time to interrupt the program.")
        dish = input("\nYour question:\n")
        messages.append(
            user_message(prompts.USER_INSTRUCTIONS.format(dish=dish))
        )

        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )
        for chunk in stream:
            print(chunk.choices[0].delta.content or "", end="", flush=True)
except KeyboardInterrupt:
    print("\n\nProgram interrupted. Thank you for using!")