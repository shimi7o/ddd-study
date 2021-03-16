from typing import Optional
from user_repository import IUserRepository
from user import User

# DBの代わり
USER_LIST = []


class DB(IUserRepository):
    def save(self, user: User) -> User:
        USER_LIST.append(user)
        return user

    def find_by_name(self, name: str) -> Optional[User]:
        for user in USER_LIST:
            if name == user.name:
                return user
        return None

    def find_by_id(self, id: str) -> Optional[User]:
        for user in USER_LIST:
            if id == user.id:
                return user
        return None