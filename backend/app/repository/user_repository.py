import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error
from app.repository.database import DatabaseRepository  # 既存のDatabaseRepositoryを継承 or 再利用

load_dotenv()

class UserRepository(DatabaseRepository):
    def create_user(self, username, email, hashed_password, role='user'):
        query = """
            INSERT INTO users (username, email, hashed_password, role)
            VALUES (%s, %s, %s, %s)
        """
        return self._execute_write_query(query, (username, email, hashed_password, role))
    
    def get_user_by_email(self, email):
        query = """
            SELECT id, username, email, hashed_password, role, created_at, updated_at
            FROM users WHERE email = %s
        """
        result = self._execute_query(query, (email,))
        if result and len(result) > 0:
            row = result[0]
            return {
                "id": row[0],
                "username": row[1],
                "email": row[2],
                "hashed_password": row[3],
                "role": row[4],
                "created_at": row[5],
                "updated_at": row[6],
            }
        return None
    
    def get_user_by_id(self, user_id):
        query = """
            SELECT id, username, email, hashed_password, role, created_at, updated_at
            FROM users WHERE id = %s
        """
        result = self._execute_query(query, (user_id,))
        if result and len(result) > 0:
            row = result[0]
            return {
                "id": row[0],
                "username": row[1],
                "email": row[2],
                "hashed_password": row[3],
                "role": row[4],
                "created_at": row[5],
                "updated_at": row[6],
            }
        return None
