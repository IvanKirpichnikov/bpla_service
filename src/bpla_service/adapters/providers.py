from typing import override

from starlette.requests import Request

from uav_service.application.provider import Provider
from uav_service.application.session.cryptographer import SessionCryptographer
from uav_service.application.session.gateway import SessionGateway
from uav_service.application.user.gateway import UserGateway
from uav_service.config import SessionConfig
from uav_service.domain.session.entity import Session
from uav_service.domain.session.errors import UnauthorizedError
from uav_service.domain.user.entity import User


class UserProvider(Provider[User]):
    def __init__(
        self,
        request: Request,
        user_gateway: UserGateway,
        session_config: SessionConfig,
        session_gateway: SessionGateway,
        session_cryptographer: SessionCryptographer,
    ) -> None:
        self._request = request
        self._user_gateway = user_gateway
        self._session_config = session_config
        self._session_gateway = session_gateway
        self._session_cryptographer = session_cryptographer
    
    @override
    async def get(self) -> User:
        session_id = self._request.cookies.get(self._session_config.cookie_key)
        if session_id is None:
            raise UnauthorizedError
        
        session = await self._session_gateway.with_id(
            self._session_cryptographer.decrypto(session_id),
        )
        session.verify()
        
        user = await self._user_gateway.with_id(session.user_id)
        
        return user


class SessionProvider(Provider[Session]):
    def __init__(
        self,
        request: Request,
        session_config: SessionConfig,
        session_gateway: SessionGateway,
        session_cryptographer: SessionCryptographer,
    ) -> None:
        self._request = request
        self._session_config = session_config
        self._session_gateway = session_gateway
        self._session_cryptographer = session_cryptographer
    
    @override
    async def get(self) -> Session:
        session_id = self._request.cookies.get(self._session_config.cookie_key)
        if session_id is None:
            raise UnauthorizedError
        
        session = await self._session_gateway.with_id(
            self._session_cryptographer.decrypto(session_id),
        )
        return session
