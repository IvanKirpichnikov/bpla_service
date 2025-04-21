from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from bpla_service.domain.uav_flight.entity import UavFlight


class UavFlightGateway(Protocol):
    @abstractmethod
    async def add(self, entity: UavFlight) -> None:
        raise NotImplementedError
    
    @abstractmethod
    async def update(self, entity: UavFlight) -> None:
        raise NotImplementedError
    
    @abstractmethod
    async def with_id(self, id: UUID) -> UavFlight:
        raise NotImplementedError


class UavFlightsGateway(Protocol):
    @abstractmethod
    async def with_user_id(self, user_id: UUID) -> list[UavFlight]:
        raise NotImplementedError
