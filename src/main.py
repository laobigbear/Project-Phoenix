import argparse
from datetime import datetime
from src.logger import get_logger

def parse_args()->argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default='David')
    parser.add_argument('--level', default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
    return parser.parse_args()

def main():
    args = parse_args()
    log = get_logger(level=args.level)
    log.info("Program Started") 
    log.info(f"User Input: {args.name}")
    log.info(f"Logging Level: {args.level}")
    log.debug("This is a debug message")
    log.info("Program Finished")

    print(f'[{datetime.now():%Y-%m-%d %H:%M:%S}] Hello, {args.name}!')

if __name__ == '__main__':
    main()