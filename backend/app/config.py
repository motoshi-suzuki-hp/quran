import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
    REFRESH_SECRET_KEY = os.getenv("REFRESH_SECRET_KEY", "default-refresh-secret")
    TOKEN_EXPIRE_HOURS = int(os.getenv("TOKEN_EXPIRE_HOURS", 3))
    DB_HOST = os.getenv("DB_HOST", "db")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DB_NAME = os.getenv("DB_NAME", "quran")
