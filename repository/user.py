from dataclasses import dataclass
import uuid


@dataclass
class User:
    __id: str
    __name: str

    def __post_init__(self) -> None:
        if not self.__id:
            raise ValueError("id is empty string")
        if not self.__name:
            raise ValueError("name is empty string")
        if len(self.__name) < 3:
            raise ValueError("nameは3文字以上です")

    def __eq__(self, other):
        # idのみで比較する
        print("__eq__")
        print(self.__id)
        print(other.__id)
        return isinstance(other, User) and (self.__id == other.__id)

    @property
    def name(self):
        print("getter")
        return self.__name

    @name.setter
    def name(self, name):
        print("setter")
        self.__name = name
