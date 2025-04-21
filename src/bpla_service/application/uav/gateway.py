from abc import abstractmethod
from typing import Iterable, Protocol
from uuid import UUID

from bpla_service.domain.uav.entity import Uav


class UavGateway(Protocol):
    @abstractmethod
    async def add(self, entity: Uav) -> None:
        raise NotImplementedError
    
    @abstractmethod
    async def update(self, entity: Uav) -> None:
        raise NotImplementedError
    
    @abstractmethod
    async def with_id(self, id: UUID) -> Uav:
        raise NotImplementedError

class UavsGateway(Protocol):
    @abstractmethod
    async def with_user_id(self, user_id: UUID) -> Iterable[Uav]:
        raise NotImplementedError
