import requests
import json

url = "http://127.0.0.1:5000/api/market"
data = {
    "symbol": "BTCUSDT",
    "side": "BUY",
    "quantity": 0.001
}

response = requests.post(url, json=data)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")