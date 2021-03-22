from abc import ABCMeta
from abc import abstractmethod
from circle import Circle
from circle_name import CircleName
from user import User


class ICircleFactory(metaclass=ABCMeta):
    @abstractmethod
    def create(name: CircleName, owner User) -> Circle:
        pass
