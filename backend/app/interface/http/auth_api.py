from flask import Blueprint, request, jsonify, g
from marshmallow import ValidationError
from interface.schemas.auth_schema import (
    SignupRequestSchema,
    SignupResponseSchema,
    LoginRequestSchema,
    LoginResponseSchema,
    RefreshRequestSchema,
    MeResponseSchema
)
from application.auth_service import AuthService
from infrastructure.persistence.user_repository import UserRepository
from domain.services.user_service import UserService
from interface.http.decorators import token_required

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()
        validated_data = SignupRequestSchema().load(data)
        
        user_id = AuthService.signup(
            username=validated_data["username"],
            email=validated_data["email"],
            plain_password=validated_data["password"],
            first_language=validated_data["first_language"],
            second_language=validated_data["second_language"],
            third_language=validated_data["third_language"],
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

@auth_blueprint.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        validated_data = LoginRequestSchema().load(data)
        email = validated_data["email"]
        password = validated_data["password"]
        (user, access_token, refresh_token), error = AuthService.login(email, password)
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

@auth_blueprint.route("/refresh", methods=["POST"])
def refresh():
    try:
        data = request.get_json()
        validated_data = RefreshRequestSchema().load(data)
        new_access_token = AuthService.refresh_token(validated_data["refresh_token"])
        if not new_access_token:
            return jsonify({"error": "Invalid or expired refresh token"}), 401
        return jsonify({"access_token": new_access_token}), 200
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_blueprint.route("/me", methods=["GET"])
@token_required
def me():
    # token_required で認証済みなら、g.user_payload にデコード済みの情報が格納されている
    user_payload = g.user_payload
    user_repo = UserRepository()
    record_dict = user_repo.get_user_by_id(user_payload["sub"])
    if not record_dict:
        return jsonify({"error": "User not found"}), 404
    user_entity = UserService.create_user_entity(record_dict)
    res_data = MeResponseSchema().dump({
        "id": user_entity.id,
        "username": user_entity.username,
        "email": user_entity.email,
        "first_language": user_entity.first_language,
        "second_language": user_entity.second_language,
        "third_language": user_entity.third_language,
        "role": user_entity.role,
    })
    return jsonify(res_data), 200
