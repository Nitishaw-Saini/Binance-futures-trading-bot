from bot.orders import OrderManager

manager = OrderManager()

response = manager.place_market_order(
    symbol="BTCUSDT",
    side="BUY",
    quantity=0.001
)

print(response)