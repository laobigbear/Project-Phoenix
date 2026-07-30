import argparse
from src.core.logger import get_logger
from src.llm.factory import LLMFactory
from src.core.decorator import timer

def parse_args()->argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default='David')
    parser.add_argument('--level', default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
    parser.add_argument('--provider', default='chatgpt', choices=['chatgpt', 'gemini'])
    return parser.parse_args()

def get_user_input():
    user_input = input("Enter your message: ")
    return user_input

def chat_loop(llm_client):
    while True:
        user_input = get_user_input()
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting the chat.")
            break
        try:
            response = llm_client.chat(user_input)
            print(f"AI Response: {response}")
        except Exception as e:
            print(f"Error occurred: {e}")

def main():
    args = parse_args()
    log = get_logger(level=args.level)
    log.info(
        "Program started | user=%s provider=%s level=%s",
        args.name,
        args.provider,
        args.level,
    )
    llm_client = LLMFactory.create(args.provider)
    chat_loop(llm_client)
    log.info("Program Finished")

if __name__ == '__main__':
    main()