from circle_repository import ICircleRepository
from user_repository import IUserRepository
from circle_factory import IICircleFactory
from circle_service import CircleService
from circle_create_command import CircleCreateCommand
from circle_join_command import CircleJoinCommand
from db import DB
import uuid
from typing import Optional


# TODO: 凝集度が高くなるようにアプリケーションサービスを分割する


class CircleApplicationService:
    user_repository: IUserRepository  # 抽象に依存
    circle_repository: ICircleRepository  # 抽象に依存
    circle_service: CircleService
    circle_factory: IICircleFactory  # 抽象に依存

    def __init__(
        self, user_repository, circle_repository, circle_service, circle_factory
    ):
        self.user_repository = user_repository
        self.circle_repository = circle_repository
        self.circle_service = circle_service
        self.circle_factory = circle_factory

    def create(self, command: CircleCreateCommand):
        owner_id = command.user_id

        user = self.user_repository.find_by_id(owner_id)

        if not user:
            raise ValueError("サークルのオーナーとなるユーザーが見つかりませんでした")

        # TODO: 排他制御

        name = CircleName(command.name)
        circle = circle_factory.create(name, owner)

        if circle_service.exists(circle):
            raise ValueError("サークルはすでに存在しています")

        circle_repository.save(circle)


    def join(self, command: CircleCreateCommand):
        


if __name__ == "__main__":
    circle_repository = DB()
    circle_service = CircleService(circle_repository)
    circle_factory = UserFactory()
    user_app_service = UserApplicationService(
        circle_repository, circle_service, circle_factory
    )
    user = user_app_service.register("tanaka")
    user_app_service.update(CircleCreateCommand(user.id, "nakata"))
    print(user_app_service.get(user.id))
