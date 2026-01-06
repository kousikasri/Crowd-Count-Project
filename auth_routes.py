from flask import Blueprint, request, jsonify
import jwt
import datetime
from functools import wraps

# Blueprint
auth_bp = Blueprint("auth", __name__)

# Dummy users (for project/demo)
USERS = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "user"
    }
}

SECRET_KEY = "super-secret-key"


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username not in USERS or USERS[username]["password"] != password:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401

    payload = {
        "username": username,
        "role": USERS[username]["role"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return jsonify({
        "success": True,
        "token": token,
        "role": USERS[username]["role"]
    })
