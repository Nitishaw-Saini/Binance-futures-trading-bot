from binance.exceptions import BinanceAPIException

from bot.client import get_client
from bot.logging_config import logger


class OrderManager:

    def __init__(self):
        self.client = get_client()

    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):

        try:

            logger.info(
                f"MARKET ORDER REQUEST | "
                f"symbol={symbol} "
                f"side={side} "
                f"quantity={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(
                f"MARKET ORDER RESPONSE | {response}"
            )

            return response

        except BinanceAPIException as e:

            logger.error(
                f"API ERROR | {str(e)}"
            )

            raise

        except Exception as e:

            logger.error(
                f"UNEXPECTED ERROR | {str(e)}"
            )

            raise

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        try:

            logger.info(
                f"LIMIT ORDER REQUEST | "
                f"symbol={symbol} "
                f"side={side} "
                f"quantity={quantity} "
                f"price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(
                f"LIMIT ORDER RESPONSE | {response}"
            )

            return response

        except BinanceAPIException as e:

            logger.error(
                f"API ERROR | {str(e)}"
            )

            raise

        except Exception as e:

            logger.error(
                f"UNEXPECTED ERROR | {str(e)}"
            )

            raise