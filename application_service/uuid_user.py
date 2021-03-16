from user import User
from user_factory import IUserFactory
import uuid

class UserFactory(IUserFactory):
    def create(self, name: str) -> User:
        id = str(uuid.uuid4())
        return User(name, id)
