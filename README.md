# Binance Futures Testnet Trading Bot

A Python-based trading bot that allows users to place Market and Limit orders on Binance Futures Testnet through both a Command Line Interface (CLI) and a Streamlit-based UI.

Features:
- BUY and SELL Orders
- Market Orders
- Limit Orders
- Input Validation
- Logging
- Error Handling
- Streamlit UI


## API Configuration

This project uses Binance Futures Testnet APIs.

To run the project, users must generate their own Binance Futures Testnet API credentials.

Create a `.env` file in the project root and add:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

For security reasons, API credentials are not included in this repository.


## Installation

Clone the repository:

```bash
git clone <repository_url>
cd trading_bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```



## Run CLI

Market Order:

```bash
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
```

Limit Order:

```bash
python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 200000
```