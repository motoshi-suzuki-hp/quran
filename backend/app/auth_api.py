from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.interface.auth_schema import (
    SignupRequestSchema,
    SignupResponseSchema,
    LoginRequestSchema,
    LoginResponseSchema,
    RefreshRequestSchema,
    MeResponseSchema
)
from app.application.auth_manager import AuthManager
from app.repository.user_repository import UserRepository
from app.domain.user_service import UserService

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()
        validated_data = SignupRequestSchema().load(data)
        
        user_id = AuthManager.signup(
            username=validated_data["username"],
            email=validated_data["email"],
            plain_password=validated_data["password"],
            role=validated_data.get("role", "user")
        )
        if not user_id:
            return jsonify({"error": "Unable to create user"}), 400
        
        response_data = SignupResponseSchema().dump({
            "message": "User created successfully",
            "user_id": user_id
        })
        return jsonify(response_data), 201

    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        validated_data = LoginRequestSchema().load(data)

        email = validated_data["email"]
        password = validated_data["password"]

        (user, access_token, refresh_token), error = AuthManager.login(email, password)
        if error:
            return jsonify({"error": error}), 401
        
        return jsonify(
            LoginResponseSchema().dump({
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role
                }
            })
        ), 200

    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth.route("/refresh", methods=["POST"])
def refresh():
    try:
        data = request.get_json()
        validated_data = RefreshRequestSchema().load(data)
        new_access_token = AuthManager.refresh_token(validated_data["refresh_token"])
        if not new_access_token:
            return jsonify({"error": "Invalid or expired refresh token"}), 401
        return jsonify({"access_token": new_access_token}), 200
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth.route("/me", methods=["GET"])
def me():
    """
    ヘッダー "Authorization: Bearer <ACCESS_TOKEN>" からユーザー情報を取得。
    """
    auth_header = request.headers.get("Authorization", None)
    if not auth_header:
        return jsonify({"error": "Missing Authorization Header"}), 401
    
    parts = auth_header.split()
    if len(parts) != 2 or parts[0] != "Bearer":
        return jsonify({"error": "Invalid Authorization header format"}), 401
    
    token = parts[1]
    decoded = AuthManager.verify_access_token(token)
    if not decoded:
        return jsonify({"error": "Invalid or expired token"}), 401
    
    # DBからユーザー情報を再取得 (token内のusername or idを利用)
    user_repo = UserRepository()
    record_dict = user_repo.get_user_by_id(decoded["sub"])
    if not record_dict:
        return jsonify({"error": "User not found"}), 404
    user_entity = UserService.create_user_entity(record_dict)

    res_data = MeResponseSchema().dump({
        "id": user_entity.id,
        "username": user_entity.username,
        "email": user_entity.email,
        "role": user_entity.role,
    })
    return jsonify(res_data), 200
