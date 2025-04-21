from dataclasses import dataclass
from datetime import datetime

from bpla_service.application.commitable import Commitable
from bpla_service.application.session.cryptographer import SessionCryptographer
from bpla_service.application.session.gateway import SessionGateway
from bpla_service.application.user.gateway import UserGateway
from bpla_service.application.user.password_hasher import PasswordHasher
from bpla_service.config import SessionConfig
from bpla_service.domain.session.entity import Session
from bpla_service.domain.user.entity import User
from bpla_service.domain.user.enums.gender_type import UserGenderType
from bpla_service.domain.user.errors import UserAlreadyExistsError, UserNotFoundError
from bpla_service.domain.user.validators import user_email_validator
from bpla_service.domain.user.value_objects.passport_data import PassportData


@dataclass
class PassportDataDs:
    issued_by: str
    date_of_issue: datetime
    subdivision_code: str
    gender: UserGenderType
    year_of_birth: datetime
    place_of_birth: str
    serial_number: str
    number: str
    snils: str
    fio: str


class LoginUser:
    def __init__(
        self,
        config: SessionConfig,
        commitable: Commitable,
        user_gateway: UserGateway,
        session_gateway: SessionGateway,
        password_hasher: PasswordHasher,
        session_cryptographer: SessionCryptographer,
    ) -> None:
        self._config = config
        self._commitable = commitable
        self._user_gateway = user_gateway
        self._password_hasher = password_hasher
        self._session_gateway = session_gateway
        self._session_cryptographer = session_cryptographer
    
    async def __call__(
        self,
        email: str,
        password: str,
        passport_data: PassportDataDs,
    ) -> str:
        user_email_validator(email)
        
        try:
            user = await self._user_gateway.with_email(email)
        except UserNotFoundError:
            pass
        else:
            raise UserAlreadyExistsError
        
        user = User.create(
            email=email,
            hashed_password=self._password_hasher.hash(password),
            passport_data=PassportData(
                fio=passport_data.fio,
                issued_by=passport_data.issued_by,
                gender=passport_data.gender,
                number=passport_data.number,
                date_of_issue=passport_data.date_of_issue,
                serial_number=passport_data.serial_number,
                year_of_birth=passport_data.year_of_birth,
                place_of_birth=passport_data.place_of_birth,
                subdivision_code=passport_data.subdivision_code,
                snils=passport_data.snils,
            ),
        )
        session = Session.create(
            user_id=user.id,
            expires_in=self._config.expires_in,
        )
        
        await self._user_gateway.add(user)
        await self._session_gateway.add(session)
        
        await self._commitable.commit()
        
        return self._session_cryptographer.crypto(session)
