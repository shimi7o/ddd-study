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

matsuoka = User(UserId(str(uuid.uuid4())), Username("松岡"))
