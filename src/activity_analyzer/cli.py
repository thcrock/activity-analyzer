import argparse
from .analyzer import analyze

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("user")
    args = parser.parse_args()
    user = args.user
    analyze(user)
