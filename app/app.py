from flask import Flask, jsonify
import logging
import os
from datetime import datetime

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "dev")

logging.basicConfig(
    level=logging.DEBUG if APP_ENV == "dev" else logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

@app.route("/")
def home():
    logger.info("Root endpoint accessed")
    return jsonify({
        "message": "Application is running",
        "environment": APP_ENV
    })

@app.route("/health")
def health():
    logger.info("Health check endpoint accessed")

    return jsonify({
        "status": "UP",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": APP_ENV
    })

if __name__ == "__main__":
    logger.info("Starting Flask application")
    app.run(host="0.0.0.0", port=5000)

