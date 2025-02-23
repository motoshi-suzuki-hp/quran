class User:
    def __init__(self, user_id, username, email, hashed_password, role='user', created_at=None, updated_at=None):
        self.id = user_id
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.role = role
        self.created_at = created_at
        self.updated_at = updated_at

    def is_admin(self):
        return self.role == 'admin'
