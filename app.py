"""
Flask REST service for DevEx assignment.
Provides basic health check and product listing endpoints.
"""

import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    """Health check endpoint."""
    return jsonify({"service": "devex-sample", "status": "ok"})


@app.get("/products")
def products():
    """Fetch products from external API."""
    try:
        response = requests.get("https://dummyjson.com/products", timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch products", "details": str(e)}), 502


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
