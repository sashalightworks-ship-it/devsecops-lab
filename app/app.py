import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(message="Hello from DevSecOps lab!", version=os.getenv("APP_VERSION", "dev"))


@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    # 0.0.0.0 - приложение слушает все интерфейсы, иначе
    # из-за пределов контейнера до него не достучаться
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))