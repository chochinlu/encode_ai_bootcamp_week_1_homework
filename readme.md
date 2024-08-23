# AI Chef Recipe Generator

This project uses OpenAI's GPT model to generate detailed recipes based on user input.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-chef-recipe-generator.git
   ```

2. Navigate to the project directory:
   ```
   cd ai-chef-recipe-generator
   ```

3. Create a virtual environment with Python 3.12:
   ```
   python3.12 -m venv venv
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

3. When prompted, enter the name of the dish you want a recipe for.

4. The AI will generate and display a detailed recipe for the requested dish.

## Environment Variables

This project uses dotenv for environment variable management. Create a `.env` file in the root directory and add the following variable:

```
OPENAI_API_KEY=your_openai_api_key_here
```

Make sure to replace `your_openai_api_key_here` with your actual OpenAI API key.

## Features

- Utilizes OpenAI's GPT model to generate recipes
- Provides detailed recipes and preparation steps for user-requested dishes
- Handles unknown dish requests gracefully
- Streams the AI's response for a more interactive experience

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).