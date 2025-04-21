from bpla_service.application.commitable import Commitable
from bpla_service.application.session.cryptographer import SessionCryptographer
from bpla_service.application.session.gateway import SessionGateway
from bpla_service.application.user.gateway import UserGateway
from bpla_service.application.user.password_hasher import PasswordHasher
from bpla_service.config import SessionConfig
from bpla_service.domain.session.entity import Session
from bpla_service.domain.user.validators import user_email_validator


class AuthUser:
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
        self._session_gateway = session_gateway
        self._password_hasher = password_hasher
        self._session_cryptographer = session_cryptographer
    
    async def __call__(
        self,
        email: str,
        password: str,
    ) -> str:
        user_email_validator(email)
        
        user = await self._user_gateway.with_email(email)
        user.ensure_deleted()
        self._password_hasher.verify(password, user.hashed_password)
        
        session = Session.create(
            user_id=user.id,
            expires_in=self._config.expires_in,
        )
        
        await self._session_gateway.add(session)
        await self._commitable.commit()
        
        return self._session_cryptographer.crypto(session)
