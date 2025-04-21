from bpla_service.application.commitable import Commitable
from bpla_service.application.provider import Provider
from bpla_service.application.session.gateway import SessionGateway
from bpla_service.domain.session.entity import Session
from bpla_service.domain.user.entity import User


class Logout:
    def __init__(
        self,
        commitable: Commitable,
        user_provider: Provider[User],
        session_provider: Provider[Session],
        session_gateway: SessionGateway,
    ) -> None:
        self._commitable = commitable
        self._user_provider = user_provider
        self._session_provider = session_provider
        self._session_gateway = session_gateway
    
    async def __call__(self) -> None:
        user = await self._user_provider.get()
        user.ensure_deleted()
        
        session = await self._session_provider.get()
        session.revoke()
        
        await self._session_gateway.update(session)
        await self._commitable.commit()
