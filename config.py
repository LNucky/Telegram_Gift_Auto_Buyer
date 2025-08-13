from dotenv import load_dotenv
import os

env = load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
MY_CHANNEL_ID = os.getenv('MY_CHANNEL_ID')

MIN_SUPPLY = os.getenv('MIN_SUPPLY')
MAX_SUPPLY = os.getenv('MAX_SUPPLY')
MIN_PRICE = os.getenv('MIN_PRICE')
MAX_PRICE = os.getenv('MAX_PRICE')

CYCLES = os.getenv("CYCLES")