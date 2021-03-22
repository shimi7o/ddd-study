from abc import ABCMeta
from abc import abstractmethod
from circle import Circle


class ICircleRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, circle) -> Circle:
        pass

    @abstractmethod
    def find_by_name(self, name) -> Circle:
        pass

    @abstractmethod
    def find_by_id(self, id) -> Circle:
        pass
