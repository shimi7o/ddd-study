from abc import ABCMeta
from abc import abstractmethod
from user import User


class IUserFactory(metaclass=ABCMeta):
    @abstractmethod
    def create(name: str) -> User:
        pass
