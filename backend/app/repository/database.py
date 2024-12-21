import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

class DatabaseRepository:
    def __init__(self):
        self.connection_config = {
            "host": os.getenv("DB_HOST", "db"),
            "port": int(os.getenv("DB_PORT", 3306)),
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASSWORD", "password"),
            "database": os.getenv("DB_NAME", "quran"),
            "charset": "utf8mb4",
        }

    def get_record_by_id(self, record_id):
        """
        指定されたIDのレコードをデータベースから取得する
        """
        try:
            connection = mysql.connector.connect(**self.connection_config)
            cursor = connection.cursor()

            query = "SELECT text, phoneme FROM phrases WHERE id = %s"
            cursor.execute(query, (record_id,))
            row = cursor.fetchone()
            print(row)

            if row:
                # レコードを辞書形式で返す
                return {"text": row[0], "phoneme": row[1]}
            return None

        except Error as e:
            print(f"Database error: {e}")
            return None

        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
