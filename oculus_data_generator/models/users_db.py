from enum import Enum


class UserType(Enum):
    DOCTOR = 0
    ADMIN = 1


class User:
    """ personal, contact and login data of the user """

    def __init__(
            self, _id: str, user_type: UserType, login: str, password: str, name: str, email: str, phone: str
    ) -> None:
        self.user_type: UserType = user_type
        self.login: str = login
        self.password: str = password
        self.name: str = name
        self.email: str = email
        self.phone: str = phone
