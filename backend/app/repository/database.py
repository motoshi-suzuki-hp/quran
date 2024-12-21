import mysql.connector
from mysql.connector import Error

class DatabaseRepository:
    def __init__(self, host="db", port=3306, user="root", password="password", database="quran", charset="utf8mb4"):
        self.connection_config = {
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "database": database,
            "charset": charset,
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
