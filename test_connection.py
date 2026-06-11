# from bot.client import get_client

# try:

#     client = get_client()

#     account_info = client.futures_account()

#     print("SUCCESS")
#     print("Connected to Binance Futures Testnet")

# except Exception as e:

#     print("ERROR")
#     print(str(e))








from bot.client import get_client

client = get_client()

balances = client.futures_account_balance()

for item in balances:

    if item["asset"] == "USDT":

        print("USDT Balance")
        print(item["balance"])