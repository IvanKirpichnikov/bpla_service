from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Iterable
from uuid import UUID

from bpla_service.application.provider import Provider
from bpla_service.application.session.gateway import SessionGateway
from bpla_service.application.uav.gateway import UavsGateway
from bpla_service.application.user.gateway import UserGateway
from bpla_service.domain.user.entity import User


@dataclass
class UavDs:
    id: UUID
    model: str
    serial_number: str
    reference_number: str
    noise_characteristics: Decimal
    created_at: datetime
    deleted_at: datetime | None


class ReadAllUavs:
    def __init__(
        self,
        user_gateway: UserGateway,
        uavs_gateway: UavsGateway,
        session_gateway: SessionGateway,
        user_provider: Provider[User],
    ) -> None:
        self._user_gateway = user_gateway
        self._uavs_gateway = uavs_gateway
        self._session_gateway = session_gateway
        self._user_provider = user_provider
    
    async def __call__(self) -> Iterable[UavDs]:
        user = await self._user_provider.get()
        user.ensure_deleted()
        
        uavs = await self._uavs_gateway.with_user_id(user.id)
        return [
            UavDs(
                id=uav.id,
                model=uav.data.model,
                serial_number=uav.data.serial_number,
                reference_number=uav.data.reference_number,
                noise_characteristics=uav.characteristics.noise_characteristics,
                created_at=uav.time_data.created_at,
                deleted_at=uav.time_data.deleted_at,
            ) for uav in uavs
        ]
