from src.client import client
from src.logger import logger

def place_market_order(symbol, side, quantity):
    """Places a market order on Binance Futures."""
    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError("Order quantity must be greater than 0.")

        logger.info(f"Attempting to place a MARKET {side} order for {quantity} {symbol}.")
        
        # This must be 'futures_create_order' for the older Client
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        logger.info("Successfully placed market order.")
        logger.info(f"Order Details: {order}")
        return order
    except Exception as e:
        logger.error(f"Error placing market order for {symbol}: {e}")
        return None