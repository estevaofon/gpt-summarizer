# Code Summarizer

This project uses OpenAI's GPT-3 model to generate summaries of given pieces of code. You input a file containing the code you want to summarize, and the script outputs a summary of what the code does.

## Prerequisites

To run this script, you'll need:

- Python 3.6 or later
- An OpenAI API key

You can obtain an OpenAI API key by creating an account on the [OpenAI website](https://www.openai.com/) and following the necessary steps.

## Installation

1. Clone this repository to your local machine.
2. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
3. Open the script file and replace `'your-openai-api-key'` with your actual OpenAI API key.

## Usage

To use the script, pass the path to a file containing the code you want to summarize as an argument when you run the script:

```bash
python summarize.py /path/to/your/code.py
```

