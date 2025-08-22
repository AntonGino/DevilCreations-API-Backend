
from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)
HF_API_KEY = os.environ.get("HF_API_KEY")

@app.route("/proxy", methods=["POST"])
def proxy():
    data = request.get_json()
    model_url = data.get("model_url")
    payload = data.get("payload")

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(model_url, headers=headers, json=payload)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
