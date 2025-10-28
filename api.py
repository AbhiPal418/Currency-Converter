from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

BASE_URL = "https://api.frankfurter.app/latest"

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Currency Converter API",
        "usage": "Send GET request to /convert?from=USD&to=INR&amount=10"
    })

@app.route('/convert', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = request.args.get('amount', type=float)

    if not all([from_currency, to_currency, amount]):
        return jsonify({"error": "Please provide 'from', 'to', and 'amount' parameters"}), 400

    response = requests.get(f"{BASE_URL}?from={from_currency}&to={to_currency}")
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch exchange rates"}), 500

    data = response.json()
    rates = data.get('rates', {})

    if to_currency not in rates:
        return jsonify({"error": f"Invalid currency code: {to_currency}"}), 400

    converted_amount = amount * rates[to_currency]
    return jsonify({
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "converted_amount": round(converted_amount, 2),
        "rate": rates[to_currency]
    })

if __name__ == '__main__':
    app.run(debug=True)
