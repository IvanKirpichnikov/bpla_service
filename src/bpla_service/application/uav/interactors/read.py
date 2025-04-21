from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from bpla_service.application.provider import Provider
from bpla_service.application.session.gateway import SessionGateway
from bpla_service.application.uav.gateway import UavGateway
from bpla_service.application.user.gateway import UserGateway
from bpla_service.domain.session.entity import Session


@dataclass
class UavDs:
    id: UUID
    model: str
    serial_number: str
    noise_characteristics: Decimal
    reference_number: str
    created_at: datetime
    deleted_at: datetime | None


class ReadUav:
    def __init__(
        self,
        uav_gateway: UavGateway,
        user_gateway: UserGateway,
        session_gateway: SessionGateway,
        session_provider: Provider[Session],
    ) -> None:
        self._uav_gateway = uav_gateway
        self._user_gateway = user_gateway
        self._session_gateway = session_gateway
        self._session_provider = session_provider
    
    async def __call__(self, uav_id: UUID) -> UavDs:
        session = await self._session_provider.get()
        session.verify()
        
        user = await self._user_gateway.with_id(session.user_id)
        user.ensure_deleted()
        
        uav = await self._uav_gateway.with_id(uav_id)
        
        return UavDs(
            id=uav.id,
            model=uav.data.model,
            created_at=uav.time_data.created_at,
            deleted_at=uav.time_data.deleted_at,
            serial_number=uav.data.serial_number,
            reference_number=uav.data.reference_number,
            noise_characteristics=uav.characteristics.noise_characteristics,
        )
