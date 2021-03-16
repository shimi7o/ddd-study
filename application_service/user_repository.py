from abc import ABCMeta
from abc import abstractmethod
from user import User


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user) -> User:
        pass

    @abstractmethod
    def find_by_name(self, userName) -> User:
        pass

    @abstractmethod
    def find_by_id(self, id) -> User:
        pass
