import logging
from dotenv import load_dotenv
from openai import OpenAI
import os
from importlib import import_module
from datetime import datetime

load_dotenv()

prompt_creator = os.getenv('PROMPT_CREATOR', 'sys')
prompts = import_module(f'prompts.{prompt_creator}')
from utils import system_message, user_message

# Create log filename with current date
log_filename = f"chat_log_{datetime.now().strftime('%Y%m%d')}.log"

# Set up logging
logging.basicConfig(filename=log_filename, level=logging.INFO, 
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

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
        
        # Record user input
        logging.info(f"User: {dish}")

        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )
        
        ai_response = ""
        for chunk in stream:
            content = chunk.choices[0].delta.content or ""
            print(content, end="", flush=True)
            ai_response += content
        
        # Record AI output
        logging.info(f"AI: {ai_response}")

except KeyboardInterrupt:
    print("\n\nProgram interrupted. Thank you for using!")