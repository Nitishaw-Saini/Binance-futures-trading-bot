# import os
# from dotenv import load_dotenv

# load_dotenv()

# API_KEY = os.getenv("API_KEY")
# API_SECRET = os.getenv("API_SECRET")

# print("API Key Loaded:", API_KEY is not None)
# print("Secret Loaded:", API_SECRET is not None)


import os

from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


def get_client():
    """
    Returns Binance Futures Testnet client
    """

    client = Client(
        API_KEY,
        API_SECRET
    )

    # Binance Futures Testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client