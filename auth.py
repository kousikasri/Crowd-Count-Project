from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token # pyright: ignore[reportMissingImports]
from users import users

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    for user in users:
        if user["username"] == username and user["password"] == password:
            token = create_access_token(
                identity=username,
                additional_claims={"role": user["role"]}
            )

            return jsonify({
                "success": True,
                "token": token,
                "role": user["role"]
            })

    return jsonify({"success": False}), 401
