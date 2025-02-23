import mysql.connector
from mysql.connector import Error
from config import Config

class DatabaseRepository:
    def __init__(self):
        self.connection_config = {
            "host": Config.DB_HOST,
            "port": Config.DB_PORT,
            "user": Config.DB_USER,
            "password": Config.DB_PASSWORD,
            "database": Config.DB_NAME,
            "charset": "utf8mb4",
        }

    def _connect(self):
        try:
            if Config.DB_HOST.startswith("/cloudsql/"):
                # UNIX ソケット経由の場合
                return mysql.connector.connect(
                    user=Config.DB_USER,
                    password=Config.DB_PASSWORD,
                    database=Config.DB_NAME,
                    unix_socket=Config.DB_HOST,
                    charset="utf8mb4"
                )
            else:
                # 通常の TCP 接続の場合
                return mysql.connector.connect(
                    host=Config.DB_HOST,
                    port=Config.DB_PORT,
                    user=Config.DB_USER,
                    password=Config.DB_PASSWORD,
                    database=Config.DB_NAME,
                    charset="utf8mb4"
                )
        except Error as e:
            print(f"Database connection error: {e}")
            return None


    def _execute_query(self, query, params=None):
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

    def _execute_write_query(self, query, params=None):
        connection = self._connect()
        if not connection:
            return None
        try:
            cursor = connection.cursor()
            cursor.execute(query, params or ())
            connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Database write query error: {e}")
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def get_record_by_surah_ayah(self, surah_id, ayah_id):
        query = "SELECT id, text, phoneme FROM phrases WHERE surah_id = %s AND ayah_id = %s"
        result = self._execute_query(query, (surah_id, ayah_id))
        if result:
            row = result[0]
            return {
                "id": row[0],
                "text": row[1],
                "phoneme": row[2]
            }
        return None
    
    def get_records_by_surah(self, surah_id):
        query = "SELECT id, ayah_id, text, phoneme FROM phrases WHERE surah_id = %s"
        result = self._execute_query(query, (surah_id,))
        if result:
            return [{
                "id": row[0],
                "ayah_id": row[1],
                "text": row[2],
                "phoneme": row[3]
            } for row in result]
        return None

    def get_records(self):
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
        return None
