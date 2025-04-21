from datetime import datetime
from uuid import UUID

from bpla_service.application.commitable import Commitable
from bpla_service.application.provider import Provider
from bpla_service.application.uav_flight.gateway import UavFlightGateway
from bpla_service.domain.uav_flight.entity import UavFlight
from bpla_service.domain.user.entity import User


class AddUavFlight:
    def __init__(
        self,
        commitable: Commitable,
        user_provider: Provider[User],
        uav_flight_gateway: UavFlightGateway,
    ) -> None:
        self._commitable = commitable
        self._user_provider = user_provider
        self._uav_flight_gateway = uav_flight_gateway
    
    async def __call__(
        self,
        uav_id: UUID,
        location: str,
        start_at: datetime,
        end_at: datetime,
    ) -> None:
        user = await self._user_provider.get()
        user.ensure_deleted()
        
        uav_flight = UavFlight.create(
            user_id=user.id,
            uav_id=uav_id,
            location=location,
            start_at=start_at,
            end_at=end_at,
        )
        await self._uav_flight_gateway.add(uav_flight)
        await self._commitable.commit()
