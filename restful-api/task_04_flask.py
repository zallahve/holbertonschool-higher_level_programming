#!/usr/bin/python3
"""
Task 04: Simple API using Flask.

Endpoints:
- GET  /              -> "Welcome to the Flask API!"
- GET  /status        -> "OK"
- GET  /data          -> JSON list of usernames (keys of users dict)
- GET  /users/<name>  -> JSON user object or 404 {"error":"User not found"}
- POST /add_user      -> Add user from JSON body with validation

Note: Users are stored in-memory only (dictionary).
Do NOT include testing data in the users dict (checker requirement).
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store: username -> user object
# IMPORTANT: Keep empty for checker (no test data committed).
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    # Return list of usernames
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    # Validate JSON body
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Build user object (store full object; ensure username is included)
    user_obj = dict(payload)
    user_obj["username"] = username

    users[username] = user_obj

    return jsonify({"message": "User added", "user": user_obj}), 201


if __name__ == "__main__":
    # Keep default host/port for local dev; checker will import/run via flask CLI.
    app.run()
