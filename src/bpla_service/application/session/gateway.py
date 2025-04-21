from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from bpla_service.domain.session.entity import Session


class SessionGateway(Protocol):
    @abstractmethod
    async def add(self, entity: Session) -> None:
        raise NotImplementedError
    
    @abstractmethod
    async def update(self, entity: Session) -> None:
        raise NotImplementedError
    
    @abstractmethod
    async def with_id(self, id: UUID) -> Session:
        raise NotImplementedError
    
    @abstractmethod
    async def with_user_id(
        self,
        user_id: UUID,
        include_deleted: bool,
    ) -> Session:
        raise NotImplementedError
