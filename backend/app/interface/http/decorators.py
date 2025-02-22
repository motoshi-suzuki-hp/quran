from functools import wraps
from flask import request, jsonify, g
from application.auth_service import AuthService

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify({"error": "Missing Authorization Header"}), 401

        parts = auth_header.split()
        if len(parts) != 2 or parts[0] != "Bearer":
            return jsonify({"error": "Invalid Authorization header format"}), 401

        token = parts[1]
        decoded = AuthService.verify_access_token(token)
        if not decoded:
            return jsonify({"error": "Invalid or expired token"}), 401

        # decoded の情報を flask.g に保存して後続処理で利用できるようにする
        g.user_payload = decoded
        return f(*args, **kwargs)
    return decorated
