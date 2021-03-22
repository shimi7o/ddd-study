from dataclasses import dataclass
import uuid


@dataclass
class CircleCreateCommand:
    __user_id: str
    __name: str = ""

    @property
    def name(self):
        return self.__name

    @property
    def user_id(self):
        return self.__user_id
