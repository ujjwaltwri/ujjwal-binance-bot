import os
from dotenv import load_dotenv
from binance.client import Client

# Load environment variables from .env file
load_dotenv()

# Get Testnet keys from environment
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')

# Check if the keys are loaded
if not api_key or not api_secret:
    raise ValueError("Binance API key and secret must be set in the .env file.")

# Create a client instance pointed at the Testnet using the older method
client = Client(api_key, api_secret, testnet=True)