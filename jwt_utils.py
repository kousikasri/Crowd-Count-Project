import jwt
from flask import request, jsonify
from functools import wraps

SECRET_KEY = "super-secret-key"

def token_required(roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = None

            if "Authorization" in request.headers:
                token = request.headers["Authorization"].split(" ")[1]

            if not token:
                token = request.args.get("token")

            if not token:
                return jsonify({"error": "Token missing"}), 401

            try:
                data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                if data["role"] not in roles:
                    return jsonify({"error": "Access denied"}), 403
            except:
                return jsonify({"error": "Invalid token"}), 401

            return f(*args, **kwargs)
        return wrapper
    return decorator
