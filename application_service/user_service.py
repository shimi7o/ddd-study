from user import User
from user_repository import UserRepository


class UserService:
    user_repository: UserRepository

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def exists(self, user: User) -> bool:
        self.user_repository.find_by_name(user.name)