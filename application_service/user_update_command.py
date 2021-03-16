from dataclasses import dataclass
import uuid


@dataclass
class UserUpdateCommand:
    __id: str
    __name: str = ""

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id
