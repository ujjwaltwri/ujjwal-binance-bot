import time
from src.market_orders import place_market_order
from src.logger import logger

def execute_twap_order(symbol, side, total_quantity, duration_minutes):
    """
    Executes a TWAP order by splitting it into smaller market orders
    placed once every minute.
    """
    try:
        total_quantity = float(total_quantity)
        duration_minutes = int(duration_minutes)
        if total_quantity <= 0 or duration_minutes <= 0:
            raise ValueError("Total quantity and duration must be positive values.")

        # For simplicity, we place one order per minute.
        num_orders = duration_minutes
        chunk_quantity = total_quantity / num_orders
        interval_seconds = 60

        logger.info(f"Starting TWAP {side} order for {total_quantity} {symbol} over {duration_minutes} minutes.")
        logger.info(f"Placing {num_orders} orders of {chunk_quantity:.8f} {symbol} each.")

        # --- Execution Loop ---
        for i in range(num_orders):
            logger.info(f"Placing TWAP chunk {i + 1}/{num_orders}...")
            order_result = place_market_order(symbol, side, f"{chunk_quantity:.8f}")
            
            if order_result is None:
                logger.error("A TWAP chunk failed to place. Aborting TWAP strategy.")
                return

            if i < num_orders - 1:
                logger.info(f"Waiting {interval_seconds} seconds until the next chunk.")
                time.sleep(interval_seconds)

        logger.info("TWAP strategy completed successfully.")

    except Exception as e:
        logger.error(f"Error during TWAP execution: {e}")