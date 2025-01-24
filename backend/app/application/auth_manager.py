import os
import jwt
import datetime
from app.repository.user_repository import UserRepository
from app.domain.user_service import UserService
from app.infrastructure.bycrypt_helper import BcryptHelper
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
REFRESH_SECRET_KEY = os.getenv("REFRESH_SECRET_KEY")
TOKEN_EXPIRE_HOURS = int(os.getenv("TOKEN_EXPIRE_HOURS", 3))

class AuthManager:
    @staticmethod
    def signup(username: str, email: str, plain_password: str, role: str = "user"):
        # パスワードハッシュ化
        hashed_password = BcryptHelper.hash_password(plain_password)
        # DB保存
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
        
        # パスワード照合
        if not BcryptHelper.check_password(plain_password, user_entity.hashed_password):
            return (None, None, None), "Invalid password"
        
        # JWT(AccessToken, RefreshToken)を発行
        access_token = AuthManager._generate_access_token(user_entity)
        refresh_token = AuthManager._generate_refresh_token(user_entity)
        return (user_entity, access_token, refresh_token), None

    @staticmethod
    def _generate_access_token(user_entity):
        # 期限 3時間 (envから取得済み)
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_EXPIRE_HOURS)
        payload = {
            "sub": str(user_entity.id),
            "username": user_entity.username,
            "role": user_entity.role,
            "exp": exp
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    @staticmethod
    def _generate_refresh_token(user_entity):
        # リフレッシュトークンの有効期限はもう少し長めでもOK (例: 7日)
        exp = datetime.datetime.utcnow() + datetime.timedelta(days=7)
        payload = {
            "sub": str(user_entity.id),
            "username": user_entity.username,
            "role": user_entity.role,
            "exp": exp
        }
        return jwt.encode(payload, REFRESH_SECRET_KEY, algorithm="HS256")

    @staticmethod
    def verify_access_token(token):
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            return decoded
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
    
    @staticmethod
    def verify_refresh_token(token):
        try:
            decoded = jwt.decode(token, REFRESH_SECRET_KEY, algorithms="HS256")
            return decoded
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    @staticmethod
    def refresh_token(refresh_token):
        decoded = AuthManager.verify_refresh_token(refresh_token)
        if not decoded:
            return None
        
        # リフレッシュトークンが正当なら、新たにアクセストークンを生成
        class TempUser:
            """
            decode結果を一時的にUserEntity風に格納
            """
            def __init__(self, user_id, username, role):
                self.id = user_id
                self.username = username
                self.role = role
        
        temp_user = TempUser(
            user_id=decoded.get("sub"),
            username=decoded.get("username"),
            role=decoded.get("role")
        )
        return AuthManager._generate_access_token(temp_user)
