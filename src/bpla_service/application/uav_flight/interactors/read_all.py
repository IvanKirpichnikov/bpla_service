from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from bpla_service.application.provider import Provider
from bpla_service.application.uav_flight.gateway import UavFlightsGateway
from bpla_service.domain.uav_flight.enums.status_type import UavFlightStatusType
from bpla_service.domain.user.entity import User


@dataclass
class UavData:
    id: UUID
    uav_id: UUID
    location: str
    start_at: datetime
    end_at: datetime
    created_at: datetime
    status: UavFlightStatusType


class ReadUavFlights:
    def __init__(
        self,
        user_provider: Provider[User],
        uav_flights_gateway: UavFlightsGateway,
    ) -> None:
        self._user_provider = user_provider
        self._uav_flights_gateway = uav_flights_gateway
    
    async def __call__(self) -> list[UavData]:
        user = await self._user_provider.get()
        user.ensure_deleted()
        
        uav_flights = await self._uav_flights_gateway.with_user_id(user.id)
        
        return [
            UavData(
                id=uav_flight.id,
                uav_id=uav_flight.uav_id,
                status=uav_flight.status,
                location=uav_flight.location,
                start_at=uav_flight.time_data.start_at,
                end_at=uav_flight.time_data.end_at,
                created_at=uav_flight.time_data.created_at,
            )
            for uav_flight in uav_flights
        ]
