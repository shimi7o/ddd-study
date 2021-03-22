from dataclasses import dataclass
import uuid
from circleid import CircleId
from circle_name import CircleName
from user import User

@dataclass
class Circle:
    __id: CircleId
    __name: CircleName
    __owner: User
    __members: User[]

    def __eq__(self, other):
        return isinstance(other, User) and (self.__id == other.__id)

    @property
    def name(self):
        print("getter")
        return self.__name

    @name.setter
    def name(self, name):
        print("setter")
        self.__name = name
