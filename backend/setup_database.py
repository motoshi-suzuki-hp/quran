import sqlite3

def setup_database(db_path="app/database/database.db"):
    """
    データベースを初期化します。
    - テーブルの作成
    - 初期データの挿入
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    try:
        # テーブルを作成
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pronunciation_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            phonemes TEXT NOT NULL
        );
        """)

        # 初期データを挿入
        initial_data = [
            ("بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ", "bɪsmɪ llɑːhɪ rrɑħmɑːnɪ rrɑħiːm"),
        ]
        cursor.executemany("""
        INSERT INTO pronunciation_records (text, phonemes)
        VALUES (?, ?);
        """, initial_data)

        connection.commit()
        print("データベースが初期化されました。")
    except Exception as e:
        print(f"データベースの初期化中にエラーが発生しました: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    setup_database()
