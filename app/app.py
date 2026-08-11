from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "DevOps Deployment Dashboard",
        "version": "1.0",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "local"),
        "application": "DevOps Deployment Dashboard"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)