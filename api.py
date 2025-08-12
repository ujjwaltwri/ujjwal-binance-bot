from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order

app = Flask(__name__)
CORS(app)

# NEW: Serve the HTML interface at the root URL
@app.route('/')
def serve_interface():
    return send_from_directory('.', 'trading_interface.html')

# Keep your existing API status route but move it to /api/status
@app.route('/api/status')
def api_status():
    return jsonify({
        "message": "Binance Bot API is running",
        "version": "1.0",
        "endpoints": {
            "/api/market": "POST - Place market orders",
            "/": "Trading Interface"
        }
    })

# Keep your existing market order endpoint
@app.route('/api/market', methods=['POST'])
def market_order_endpoint():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
            
        symbol = data.get('symbol')
        side = data.get('side')
        quantity = data.get('quantity')
        
        if not all([symbol, side, quantity]):
            return jsonify({"error": "Missing required fields: symbol, side, quantity"}), 400
            
        result = place_market_order(symbol, side, quantity)
        
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Failed to place market order"}), 400
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)