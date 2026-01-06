from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/dashboard", methods=["GET"])
@jwt_required()
def admin_dashboard():
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({"msg": "Admins only"}), 403

    return jsonify({"msg": "Admin dashboard data"})
