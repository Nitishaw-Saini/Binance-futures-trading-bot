from bot.validators import *

print(validate_side("buy"))
print(validate_side("SELL"))

print(validate_order_type("market"))

print(validate_quantity("0.001"))

print(validate_price("90000"))