from bot.orders import OrderManager

manager = OrderManager()

response = manager.place_limit_order(
    symbol="BTCUSDT",
    side="SELL",
    quantity=0.001,
    price=200000
)

print(response)