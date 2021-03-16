from dataclasses import dataclass
import uuid


@dataclass
class UserData:
    __name: str
    __id: str

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id
