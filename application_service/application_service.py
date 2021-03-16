from user_repository import IUserRepository
from user_factory import IUserFactory
from user_service import UserService
from user import User
from user_data import UserData
from user_update_command import UserUpdateCommand
from db import DB
from uuid_user import UserFactory
import uuid
from typing import Optional


# TODO: 凝集度が高くなるようにアプリケーションサービスを分割する


class UserApplicationService:
    user_repository: IUserRepository  # 抽象に依存
    user_service: UserService
    user_factory: IUserFactory  # 抽象に依存

    def __init__(self, user_repository, user_service, user_factory):
        self.user_repository = user_repository
        self.user_service = user_service
        self.user_factory = user_factory

    def register(self, name: str) -> User:
        user = self.user_factory.create(name)

        if self.user_service.exists(user):
            raise ValueError("すでに存在するユーザー名です")

        # TODO: 排他制御

        return user_repository.save(user)

    # TODO: 引数をIDにする
    def get(self, id: str) -> Optional[UserData]:
        user = user_repository.find_by_id(id)
        return UserData(user.name, user.id)

    def update(self, command: UserUpdateCommand):
        user = user_repository.find_by_id(command.id)
        if command.name:
            user.name = command.name
        user_repository.save(user)


if __name__ == "__main__":
    user_repository = DB()
    user_service = UserService(user_repository)
    user_factory = UserFactory()
    user_app_service = UserApplicationService(
        user_repository, user_service, user_factory
    )
    user = user_app_service.register("tanaka")
    user_app_service.update(UserUpdateCommand(user.id, "nakata"))
    print(user_app_service.get(user.id))
