from flask import Flask, jsonify
import os
import time

app = Flask(__name__)


@app.route("/")
def home():
    return "Cloud app running"


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/load")
def load():
    # CPU-heavy work to simulate load
    start = time.time()
    total = sum(i * i for i in range(3_000_000))
    elapsed = round(time.time() - start, 3)
    return jsonify(result=total, compute_seconds=elapsed)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    