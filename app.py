import streamlit as st

from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

st.set_page_config(
    page_title="Trading Bot",
    page_icon="📈"
)

st.title("📈 Binance Futures Testnet Trading Bot")

symbol = st.text_input(
    "Trading Symbol",
    value="BTCUSDT"
)

side = st.selectbox(
    "Side",
    ["BUY", "SELL"]
)

order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT"]
)

quantity = st.number_input(
    "Quantity",
    min_value=0.001,
    value=0.001
)

price = None

if order_type == "LIMIT":

    price = st.number_input(
        "Limit Price",
        min_value=1.0,
        value=100000.0
    )

if st.button("Place Order"):

    try:

        side = validate_side(side)

        order_type = validate_order_type(
            order_type
        )

        quantity = validate_quantity(
            quantity
        )

        if order_type == "LIMIT":

            price = validate_price(price)

        manager = OrderManager()

        if order_type == "MARKET":

            response = manager.place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            response = manager.place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        # st.success(
        #     "Order placed successfully!"
        # )

        # st.subheader(
        #     "Order Response"
        # )

        # st.json(
        #     {
        #         "orderId":
        #             response.get("orderId"),

        #         "status":
        #             response.get("status"),

        #         "executedQty":
        #             response.get(
        #                 "executedQty"
        #             ),

        #         "avgPrice":
        #             response.get(
        #                 "avgPrice"
        #             )
        #     }
        # )
        st.success("✅ Order placed successfully!")
        st.markdown("---")
        st.subheader("📋 Order Summary")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                label="Order ID",
                value=response.get("orderId", "N/A")
                )
            
            st.metric(
                label="Status",
                value=response.get("status", "N/A")
                )
            with col2:
                st.metric(
                    label="Executed Qty",
                    value=response.get("executedQty", "N/A")
                    )
                st.metric(
                    "Avg Price",
                    response.get("avgPrice") or "Pending"
                    )
                # st.metric(
                #     label="Average Price",
                #     value=response.get("avgPrice", "N/A")
                #     )
                with st.expander("🔍 View Full API Response"):
                    st.json(response)
    except Exception as e:
        st.error(str(e))




from bot.client import get_client

client = get_client()

balances = client.futures_account_balance()

for balance in balances:

    if balance["asset"] == "USDT":

        st.metric(
            "USDT Balance",
            balance["balance"]
        )


