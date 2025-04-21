import argon2
from argon2.exceptions import Argon2Error

from bpla_service.domain.user.errors import UserPasswordNotValidError


class PasswordHasher:
    def __init__(self, password_hasher: argon2.PasswordHasher) -> None:
        self._password_hasher = password_hasher
    
    def hash(self, password: str) -> str:
        return self._password_hasher.hash(password)
    
    def verify(self, password: str, hashed_password: str) -> None:
        try:
            self._password_hasher.verify(hashed_password, password)
        except Argon2Error as e:
            raise UserPasswordNotValidError from e
