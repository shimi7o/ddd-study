import uuid
from dataclasses import dataclass

@dataclass(frozen=True)
class UserId:
    value: str


@dataclass(frozen=True)
class Username:
    username: str


@dataclass
class User:
    user_id: UserId
    username: Username

class UserService:
    def is_duplicated(self, user: User) -> bool:
        # 自らのユーザのみ重複判断できる
        return user.username in USER_LIST


# DB代わりのリスト
USER_LIST = [Username("松岡"), Username("松田"), Username("松井")]

matsuoka = User(UserId(str(uuid.uuid4())), Username("松岡"))
UserService().is_duplicated(matsuoka)