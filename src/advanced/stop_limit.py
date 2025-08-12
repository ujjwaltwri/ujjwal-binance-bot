from src.client import client
from src.logger import logger

def place_stop_limit_order(symbol, side, quantity, price, stop_price):
    """
    Places a Stop-Limit order on Binance Futures.
    This triggers a limit order when a stop price is hit.
    """
    try:
        quantity = float(quantity)
        price = float(price)
        stop_price = float(stop_price)
        if quantity <= 0 or price <= 0 or stop_price <= 0:
            raise ValueError("Order quantity, price, and stop price must be greater than 0.")

        logger.info(f"Attempting to place a STOP-LIMIT {side} order for {quantity} {symbol} with stop price {stop_price} and limit price {price}.")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='STOP',
            timeInForce='GTC',
            quantity=quantity,
            price=str(price),
            stopPrice=str(stop_price)
        )
        
        logger.info("Successfully placed stop-limit order.")
        logger.info(f"Order Details: {order}")
        return order

    except Exception as e:
        logger.error(f"Error placing stop-limit order for {symbol}: {e}")
        return None