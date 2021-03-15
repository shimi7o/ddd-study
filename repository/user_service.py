from user import User


class UserService:
    def exists(self, user: User) -> bool:
        for u in USER_LIST:
            if u.name == user.name:
                return True
        return False