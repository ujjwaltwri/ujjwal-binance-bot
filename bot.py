import argparse
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit_order
from src.advanced.twap import execute_twap_order

def main():
    parser = argparse.ArgumentParser(description="A CLI-based trading bot for Binance Futures.")
    subparsers = parser.add_subparsers(dest='command', help='Available commands', required=True)

    # --- Market Order Command ---
    market_parser = subparsers.add_parser('market', help='Place a market order.')
    market_parser.add_argument('symbol', type=str, help='Trading symbol (e.g., BTCUSDT)')
    market_parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order side')
    market_parser.add_argument('quantity', type=float, help='Order quantity')

    # --- Limit Order Command ---
    limit_parser = subparsers.add_parser('limit', help='Place a limit order.')
    limit_parser.add_argument('symbol', type=str, help='Trading symbol (e.g., BTCUSDT)')
    limit_parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order side')
    limit_parser.add_argument('quantity', type=float, help='Order quantity')
    limit_parser.add_argument('price', type=float, help='Order price')
    
    # --- Stop-Limit Order Command ---
    stop_limit_parser = subparsers.add_parser('stoplimit', help='Place a stop-limit order.')
    stop_limit_parser.add_argument('symbol', type=str, help='Trading symbol (e.g., BTCUSDT)')
    stop_limit_parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order side')
    stop_limit_parser.add_argument('quantity', type=float, help='Order quantity')
    stop_limit_parser.add_argument('price', type=float, help='The price of the limit order once triggered')
    stop_limit_parser.add_argument('stop_price', type=float, help='The price that triggers the limit order')
    
    # --- TWAP Order Command ---
    twap_parser = subparsers.add_parser('twap', help='Execute a TWAP strategy.')
    twap_parser.add_argument('symbol', type=str, help='Trading symbol (e.g., BTCUSDT)')
    twap_parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order side')
    twap_parser.add_argument('total_quantity', type=float, help='The total quantity to trade')
    twap_parser.add_argument('duration_minutes', type=int, help='The total duration in minutes to execute the order')

    args = parser.parse_args()

    # --- Execute the command ---
    if args.command == 'market':
        place_market_order(args.symbol, args.side, args.quantity)
    elif args.command == 'limit':
        place_limit_order(args.symbol, args.side, args.quantity, args.price)
    elif args.command == 'stoplimit':
        place_stop_limit_order(args.symbol, args.side, args.quantity, args.price, args.stop_price)
    elif args.command == 'twap':
        execute_twap_order(args.symbol, args.side, args.total_quantity, args.duration_minutes)

if __name__ == "__main__":
    main()