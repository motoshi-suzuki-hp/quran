import bcrypt
from app.domain.user import User
from app.repository.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, email: str, password: str, user_name: str) -> User:
        # 既存ユーザー確認
        existing_user = self.user_repository.find_by_email(email)
        if existing_user:
            raise ValueError("User with this email already exists.")

        # パスワードハッシュ
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        # Userエンティティ生成
        user = User(
            id=0,  # DB側で自動採番される
            email=email,
            password_hash=hashed_password,
            user_name=user_name,
            created_at=None,  # DBが設定
            updated_at=None   # DBが設定
        )

        # DBに保存
        new_user = self.user_repository.create_user(user)
        return new_user

    def login(self, email: str, password: str) -> User:
        user = self.user_repository.find_by_email(email)
        if not user:
            raise ValueError("User does not exist.")

        # パスワード照合
        if not bcrypt.checkpw(password.encode("utf-8"), user.password_hash.encode("utf-8")):
            raise ValueError("Invalid password.")

        # ログイン成功
        return user
