from flask import Flask, request, jsonify
import requests

app = Flask(name)  # FIXED THIS LINE

INSTAGRAM_URL = "https://www.instagram.com/"

def check_username(username):
    url = f"{INSTAGRAM_URL}{username}/"
    response = requests.get(url)
    return response.status_code == 404  # Agar 404 aaya to username available hai

@app.route("/")
def home():
    return "Instagram Username Checker is Running!"

@app.route("/check", methods=["GET"])
def check():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Please provide a username"}), 400

    is_available = check_username(username)
    return jsonify({"username": username, "available": is_available})

if name == "main":  # FIXED THIS LINE
    app.run(debug=True, host="0.0.0.0", port=5000)