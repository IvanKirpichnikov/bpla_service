from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from bpla_service.domain.user.entity import User


class UserGateway(Protocol):
    @abstractmethod
    async def add(self, entity: User) -> None:
        raise NotImplementedError
    
    @abstractmethod
    async def with_id(self, id: UUID) -> User:
        raise NotImplementedError
    
    @abstractmethod
    async def with_email(self, email: str) -> User:
        raise NotImplementedError
    
    @abstractmethod
    async def update(self, entity: User) -> None:
        raise NotImplementedError
