from src.client import client
from src.logger import logger

def place_limit_order(symbol, side, quantity, price):
    """Places a limit order on Binance Futures."""
    try:
        quantity = float(quantity)
        price = float(price)
        if quantity <= 0 or price <= 0:
            raise ValueError("Order quantity and price must be greater than 0.")

        logger.info(f"Attempting to place a LIMIT {side} order for {quantity} {symbol} at price {price}.")
        
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            timeInForce='GTC',
            quantity=quantity,
            price=str(price)
        )
        logger.info("Successfully placed limit order.")
        logger.info(f"Order Details: {order}")
        return order
    except Exception as e:
        logger.error(f"Error placing limit order for {symbol}: {e}")
        return None