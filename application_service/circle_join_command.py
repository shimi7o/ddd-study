from dataclasses import dataclass
import uuid


@dataclass
class CircleJoinCommand:
    __user_id: str
    __circle_id: str = ""

    @property
    def user_id(self):
        return self.__user_id

    @property
    def circle_id(self):
        return self.__circle_id
