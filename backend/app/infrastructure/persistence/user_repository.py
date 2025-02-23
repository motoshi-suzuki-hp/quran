from infrastructure.persistence.database import DatabaseRepository

class UserRepository(DatabaseRepository):
    def create_user(self, username, email, hashed_password, first_language, second_language, third_language, role='user'):
        query = """
            INSERT INTO users (username, email, hashed_password, first_language, second_language, third_language, role)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        return self._execute_write_query(query, (username, email, hashed_password, first_language, second_language, third_language, role))
    
    def get_user_by_email(self, email):
        query = """
            SELECT id, username, email, hashed_password, first_language, second_language, third_language, role, created_at, updated_at
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
                "first_language": row[4],
                "second_language": row[5],
                "third_language": row[6],
                "role": row[7],
                "created_at": row[8],
                "updated_at": row[9],
            }
        return None
    
    def get_user_by_id(self, user_id):
        query = """
            SELECT id, username, email, hashed_password, first_language, second_language, third_language, role, created_at, updated_at
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
                "first_language": row[4],
                "second_language": row[5],
                "third_language": row[6],
                "role": row[7],
                "created_at": row[8],
                "updated_at": row[9],
            }
        return None
