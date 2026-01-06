from flask import Blueprint, jsonify
from user.user_store import get_users, toggle_user, change_role, delete_user

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["GET"])
def list_users():
    return jsonify(get_users())

@user_bp.route("/users/toggle/<username>", methods=["POST"])
def toggle(username):
    user = toggle_user(username)
    return jsonify(user)

@user_bp.route("/users/role", methods=["POST"])
def update_role():
    data = request.json
    user = change_role(data["username"], data["role"])
    return jsonify(user)

@user_bp.route("/users/delete/<username>", methods=["DELETE"])
def delete(username):
    delete_user(username)
    return {"msg": "User deleted"}
