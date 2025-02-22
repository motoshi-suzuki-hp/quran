import jwt
import datetime
from infrastructure.persistence.user_repository import UserRepository
from domain.services.user_service import UserService
from infrastructure.services.bcrypt_helper import BcryptHelper
from config import Config

class AuthService:
    @staticmethod
    def signup(username: str, email: str, plain_password: str, role: str = "user"):
        hashed_password = BcryptHelper.hash_password(plain_password)
        user_repo = UserRepository()
        user_id = user_repo.create_user(username, email, hashed_password, role)
        return user_id

    @staticmethod
    def login(email: str, plain_password: str):
        user_repo = UserRepository()
        record_dict = user_repo.get_user_by_email(email)
        if not record_dict:
            return (None, None, None), "User not found"
        
        user_entity = UserService.create_user_entity(record_dict)
        
        if not BcryptHelper.check_password(plain_password, user_entity.hashed_password):
            return (None, None, None), "Invalid password"
        
        access_token = AuthService._generate_access_token(user_entity)
        refresh_token = AuthService._generate_refresh_token(user_entity)
        return (user_entity, access_token, refresh_token), None

    @staticmethod
    def _generate_access_token(user_entity):
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=Config.TOKEN_EXPIRE_HOURS)
        payload = {
            "sub": str(user_entity.id),
            "username": user_entity.username,
            "role": user_entity.role,
            "exp": exp
        }
        return jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")

    @staticmethod
    def _generate_refresh_token(user_entity):
        exp = datetime.datetime.utcnow() + datetime.timedelta(days=7)
        payload = {
            "sub": str(user_entity.id),
            "username": user_entity.username,
            "role": user_entity.role,
            "exp": exp
        }
        return jwt.encode(payload, Config.REFRESH_SECRET_KEY, algorithm="HS256")

    @staticmethod
    def verify_access_token(token):
        try:
            decoded = jwt.decode(token, Config.SECRET_KEY, algorithms="HS256")
            return decoded
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    @staticmethod
    def verify_refresh_token(token):
        try:
            decoded = jwt.decode(token, Config.REFRESH_SECRET_KEY, algorithms="HS256")
            return decoded
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    @staticmethod
    def refresh_token(refresh_token):
        decoded = AuthService.verify_refresh_token(refresh_token)
        if not decoded:
            return None
        # 一時的なユーザーオブジェクトを生成して新規アクセストークン発行
        class TempUser:
            def __init__(self, user_id, username, role):
                self.id = user_id
                self.username = username
                self.role = role
        temp_user = TempUser(
            user_id=decoded.get("sub"),
            username=decoded.get("username"),
            role=decoded.get("role")
        )
        return AuthService._generate_access_token(temp_user)
