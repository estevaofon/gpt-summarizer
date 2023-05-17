import os
import openai
import argparse
from dotenv import load_dotenv

load_dotenv()
# Load your API key from an environment variable or secret management service
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


def summarize_code(code):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "Você é um assistente prestativo"},
            {"role": "user", "content": f"Você pode resumir o que esse código faz? \n\n {code}"},
        ]
    )

    return response['choices'][0]['message']['content']

def read_code_from_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    return code

def main():
    parser = argparse.ArgumentParser(description='Summarize the given code.')
    parser.add_argument('file_path', type=str, help='The path to the code file to summarize.')
    
    args = parser.parse_args()
    
    code = read_code_from_file(args.file_path)
    summary = summarize_code(code)
    print(summary)

# If the script is run directly, execute the main function
if __name__ == "__main__":
    main()
