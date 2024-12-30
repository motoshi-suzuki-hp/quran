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

    def _connect(self):
        """
        データベース接続を確立する。
        """
        try:
            return mysql.connector.connect(**self.connection_config)
        except Error as e:
            print(f"Database connection error: {e}")
            return None

    def _execute_query(self, query, params=None):
        """
        クエリを実行し、結果を返す。
        """
        connection = self._connect()
        if not connection:
            return None

        try:
            cursor = connection.cursor()
            cursor.execute(query, params or ())
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Database query error: {e}")
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_record_by_surah_ayah(self, surah_id, ayah_id):
        """
        指定されたIDのレコードを取得する。
        """
        query = "SELECT id, text, phoneme, audio_path FROM phrases WHERE surah_id = %s AND ayah_id = %s"
        result = self._execute_query(query, (surah_id, ayah_id))

        if result:
            row = result[0]  # fetchone の代替
            return {
                "id": row[0], 
                "text": row[1], 
                "phoneme": row[2],
                "audio_path": row[3]
            }
        return {"error": "Phrase not found"}, 404
    
    def get_records_by_surah(self, surah_id):
        """
        指定されたIDのレコードを取得する。
        """
        query = "SELECT id, ayah_id, text, phoneme FROM phrases WHERE surah_id = %s"
        result = self._execute_query(query, (surah_id,))

        if result:
            return [{
                "id": row[0], 
                "ayah_id": row[1],
                "text": row[2], 
                "phoneme": row[3]
            } for row in result]
        return {"error": "Phrase not found"}, 404

    def get_records(self):
        """
        すべてのレコードを取得する。
        """
        query = "SELECT id, surah_id, ayah_id, text, phoneme FROM phrases"
        result = self._execute_query(query)

        if result:
            return [{
                "id": row[0], 
                "surah_id": row[1], 
                "ayah_id": row[2], 
                "text": row[3], 
                "phoneme": row[4]
                } for row in result]
        return {"error": "Phrase not found"}, 404
