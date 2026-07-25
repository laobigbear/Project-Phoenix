import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default='David')
    args = parser.parse_args()

    print(f'[{datetime.now():%Y-%m-%d %H:%M:%S}] Hello, {args.name}!')

if __name__ == '__main__':
    main()