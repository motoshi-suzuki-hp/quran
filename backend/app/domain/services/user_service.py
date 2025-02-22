from domain.models.user import User

class UserService:
    @staticmethod
    def create_user_entity(record_dict):
        if not record_dict:
            return None
        return User(
            user_id=record_dict["id"],
            username=record_dict["username"],
            email=record_dict["email"],
            hashed_password=record_dict["hashed_password"],
            role=record_dict["role"],
            created_at=record_dict.get("created_at"),
            updated_at=record_dict.get("updated_at")
        )
