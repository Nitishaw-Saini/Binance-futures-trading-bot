import click

from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


@click.command()

@click.option(
    "--symbol",
    required=True,
    help="Trading pair"
)

@click.option(
    "--side",
    required=True,
    help="BUY or SELL"
)

@click.option(
    "--order_type",
    required=True,
    help="MARKET or LIMIT"
)

@click.option(
    "--quantity",
    required=True,
    type=float
)

@click.option(
    "--price",
    required=False,
    type=float
)

def main(
    symbol,
    side,
    order_type,
    quantity,
    price
):

    try:

        side = validate_side(side)

        order_type = validate_order_type(
            order_type
        )

        quantity = validate_quantity(
            quantity
        )

        if order_type == "LIMIT":

            if price is None:

                raise ValueError(
                    "LIMIT order requires --price"
                )

            price = validate_price(price)

        print("\n====================")
        print("ORDER REQUEST")
        print("====================")

        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Order Type : {order_type}")
        print(f"Quantity   : {quantity}")

        if price:
            print(f"Price      : {price}")

        manager = OrderManager()

        if order_type == "MARKET":

            response = (
                manager.place_market_order(
                    symbol,
                    side,
                    quantity
                )
            )

        else:

            response = (
                manager.place_limit_order(
                    symbol,
                    side,
                    quantity,
                    price
                )
            )

        print("\n====================")
        print("ORDER RESPONSE")
        print("====================")

        print(
            f"Order ID     : "
            f"{response.get('orderId')}"
        )

        print(
            f"Status       : "
            f"{response.get('status')}"
        )

        print(
            f"Executed Qty : "
            f"{response.get('executedQty')}"
        )

        print(
            f"Average Price: "
            f"{response.get('avgPrice')}"
        )

        print("\nSUCCESS")

    except Exception as e:

        print(
            f"\nFAILED: {str(e)}"
        )


if __name__ == "__main__":
    main()