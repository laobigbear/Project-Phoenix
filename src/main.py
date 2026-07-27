import argparse
from datetime import datetime
from logger import logger


def main():
    log = logger().get_logger()
    log.info("Program Started")
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default='David')
    args = parser.parse_args()
    log.info(f"User Input: {args.name}")
    log.info("Program Finished")

    print(f'[{datetime.now():%Y-%m-%d %H:%M:%S}] Hello, {args.name}!')

if __name__ == '__main__':
    main()