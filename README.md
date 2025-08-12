# Binance Futures Trading Bot

This project is a command-line interface (CLI) trading bot developed for the Binance USDT-M Futures market. It supports various order types for executing trades programmatically and features structured logging for all actions.

## Features

* **Core Orders:**
    * Market Orders
    * Limit Orders
* **Advanced Orders:**
    * Stop-Limit Orders
    * TWAP (Time-Weighted Average Price) Strategy
* **Logging:** All order placements, executions, and errors are logged to `bot.log`.

## Project Structure

```
your_name_binance_bot/
├── src/
│   ├── advanced/
│   │   ├── stop_limit.py
│   │   └── twap.py
│   ├── client.py
│   ├── limit_orders.py
│   ├── logger.py
│   └── market_orders.py
├── .env
├── .gitignore
├── bot.log
├── bot.py
├── README.md
├── report.pdf
└── requirements.txt
```

## Setup and Installation

Follow these steps to set up and run the bot.

### 1. Clone the Repository
```bash
git clone https://github.com/ujjwaltwri/ujjwal-binance-bot
cd your_name-binance-bot
```

### 2. Create a Virtual Environment
```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
The bot requires API keys from the Binance Testnet to function.

* Create a file named `.env` in the project's root directory.
* Add your Testnet API Key and Secret Key to the file like this:

```
# .env file
BINANCE_API_KEY='your_testnet_api_key_here'
BINANCE_API_SECRET='your_testnet_secret_key_here'
```

## Usage

All commands are run from the project's root directory using `bot.py`.

### Place a Market Order
```bash
python bot.py market [SYMBOL] [SIDE] [QUANTITY]
# Example:
python bot.py market BTCUSDT BUY 0.002
```

### Place a Limit Order
```bash
python bot.py limit [SYMBOL] [SIDE] [QUANTITY] [PRICE]
# Example:
python bot.py limit BTCUSDT SELL 0.002 115000
```

### Place a Stop-Limit Order
```bash
python bot.py stoplimit [SYMBOL] [SIDE] [QUANTITY] [PRICE] [STOP_PRICE]
# Example (Stop-Loss):
python bot.py stoplimit BTCUSDT SELL 0.002 99000 99500
```

### Execute a TWAP Strategy
```bash
python bot.py twap [SYMBOL] [SIDE] [TOTAL_QUANTITY] [DURATION_MINUTES]
# Example:
python bot.py twap BTCUSDT BUY 0.006 3
```