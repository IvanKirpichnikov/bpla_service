from __future__ import annotations

from datetime import datetime, UTC
from uuid import UUID, uuid4

from bpla_service.domain.user.errors import UserDeletedError, UserPasswordNotValidError
from bpla_service.domain.user.value_objects.passport_data import PassportData
from bpla_service.domain.user.value_objects.time_data import UserTimeData


class User:
    def __init__(
        self,
        id: UUID,
        email: str,
        hashed_password: str,
        time_data: UserTimeData,
        passport_data: PassportData,
    ) -> None:
        self._id = id
        self._email = email
        self._time_data = time_data
        self._passport_data = passport_data
        self._hashed_password = hashed_password
    
    def __repr__(self) -> str:
        return (f"User(id={self._id}, passport_data={self._passport_data}, "
                f"time_data={self._time_data}, hashed_password={self._hashed_password}, "
                f"email={self._email})")
    
    @classmethod
    def create(
        cls,
        email: str,
        hashed_password: str,
        passport_data: PassportData,
    ) -> User:
        return cls(
            id=uuid4(),
            email=email,
            passport_data=passport_data,
            hashed_password=hashed_password,
            time_data=UserTimeData(created_at=datetime.now(tz=UTC)),
        )
    
    @property
    def id(self) -> UUID:
        return self._id
    
    @property
    def time_data(self) -> UserTimeData:
        return self._time_data
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def hashed_password(self) -> str:
        return self._hashed_password
    
    @hashed_password.setter
    def hashed_password(self, hashed_password: str) -> None:
        self._hashed_password = hashed_password
    
    @property
    def passport_data(self) -> PassportData:
        return self._passport_data
    
    def password_verification(self, hashed_password: str) -> None:
        if self._hashed_password != hashed_password:
            raise UserPasswordNotValidError
    
    def ensure_deleted(self) -> None:
        if self._time_data.deleted_at:
            raise UserDeletedError
