import logging
import os

from dotenv import load_dotenv

# logging config
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")

# load environment
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


if __name__ == '__main__':
    logging.info('Environment loaded')
