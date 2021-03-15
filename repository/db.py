from typing import Optional
from user_repository import UserRepository
from user import User

# DBの代わり
USER_LIST = []


class DB(UserRepository):
    def save(self, user: User):
        USER_LIST.append(user)

    def find(self, name: str) -> Optional[User]:
        for user in USER_LIST:
            if name == user.name:
                return user
        return None