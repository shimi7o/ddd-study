from circle import Circle
from circle_repository import ICircleRepository


class CircleService:
    circle_repository: ICircleRepository

    def __init__(self, circle_repository):
        self.circle_repository = circle_repository

    def exists(self, circle: Circle) -> bool:
        self.circle_repository.find_by_name(circle.name)