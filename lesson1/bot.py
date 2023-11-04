import os

from dotenv import load_dotenv, find_dotenv

name = "psycotricks"

load_dotenv(find_dotenv())
token = os.environ.get("TOKEN")

if __name__ == '__main__':
    print(token)
