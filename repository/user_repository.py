from abc import ABCMeta
from abc import abstractmethod
from user import User

class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user):
        pass

    @abstractmethod
    def find(self, userName) -> User:
        pass
