# AI Multi-Role Assistant Generator

This project uses OpenAI's GPT model to generate responses for various roles, including chef, travel advisor, and programmer.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:


2. Navigate to the project directory:


3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set up your environment variables (see [Environment Variables](#environment-variables) section).

2. Run the application:
   ```
   python app.py
   ```

3. Enter your question or request when prompted.

4. The AI will generate and display the appropriate response.

## Logging

This application includes a logging feature that records all user inputs and AI responses. The log file is created in the same directory as the application, with the filename format `chat_log_YYYYMMDD.log`, where YYYYMMDD represents the current date.

Each log entry includes a timestamp, followed by either the user's input or the AI's response. This feature allows you to review past conversations and track the AI's performance over time.

## Environment Variables

This project uses dotenv for environment variable management. Create a `.env` file in the root directory and add the following variables:

```
OPENAI_API_KEY=your_openai_api_key_here
MODEL=gpt-4o-mini
PROMPT_CREATOR=sys
```

Make sure to replace the following:
- `your_openai_api_key_here`: Replace with your actual OpenAI API key.
- `gpt-4o-mini`: Can be changed to other supported OpenAI models as needed.
- `sys`: Can be changed to other appropriate prompt creator identifiers.


## Prompt Creators

This project supports multiple prompt creators, which can be selected by changing the `PROMPT_CREATOR` variable in the `.env` file. Currently supported prompt creators include:

- `sys`: The default system prompt creator, providing basic chef role and recipe instructions.
- `park`: A specially designed Chinese cuisine chef role, skilled in Taiwanese cuisine, offering more friendly and detailed recipe guidance.

Each prompt creator is defined in a corresponding Python file within the `prompts` folder. For example, `sys.py` and `park.py`.

### Prompt Creator File Structure

Each prompt creator file should contain the following variables:

- `CHEF_DESCRIPTION`: Defines the chef's role and characteristics.
- `RECIPE_INSTRUCTIONS`: Provides specific instructions for recipe responses.
- `USER_INSTRUCTIONS`: A template for formatting user input.

To use a specific prompt creator, set the `PROMPT_CREATOR` variable in the `.env` file to the corresponding file name (without the `.py` extension). For example:


### Variable Descriptions

- `OPENAI_API_KEY`: Your OpenAI API key for accessing OpenAI services.
- `MODEL`: Specifies the OpenAI model to use. Default is `gpt-4o-mini`, but you can change it according to your needs.
- `PROMPT_CREATOR`: Used to identify the creator or source of the prompts. Default is `sys` (system).

Note that the `.env` file contains sensitive information and should not be committed to version control.
## Features

- Utilizes OpenAI's GPT model to generate responses
- Provides detailed answers based on user input
- Handles unknown requests gracefully
- Streams the AI's response for a more interactive experience

## Project Structure

- `app.py`: Main application file
- `prompts/`: Directory containing prompt files for different roles
- `utils.py`: Contains shared utility functions
- `requirements.txt`: Lists project dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).