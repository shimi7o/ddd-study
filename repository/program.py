from user_repository import UserRepository
from user import User
from db import DB
import uuid
from typing import Optional


class Program:
    user_repository: UserRepository

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, user_name: str):
        user = User(str(uuid.uuid4()), user_name)

		# TODO: 重複確認

        user_repository.save(user)

    def find_user(self, user_name: str) -> Optional[User]:
        return user_repository.find(user_name)


if __name__ == "__main__":
    user_repository = DB()
    program = Program(user_repository)
    program.create_user("tanaka")
    print(program.find_user("tanaka"))
