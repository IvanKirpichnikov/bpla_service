from decimal import Decimal

from bpla_service.application.commitable import Commitable
from bpla_service.application.provider import Provider
from bpla_service.application.uav.gateway import UavGateway
from bpla_service.domain.uav.entity import Uav
from bpla_service.domain.user.entity import User


class AddUav:
    def __init__(
        self,
        commitable: Commitable,
        uav_gateway: UavGateway,
        user_provider: Provider[User],
    ) -> None:
        self._commitable = commitable
        self._uav_gateway = uav_gateway
        self._user_provider = user_provider
    
    async def __call__(
        self,
        model: str,
        serial_number: str,
        reference_number: str,
        noise_characteristics: Decimal,
    ) -> None:
        user = await self._user_provider.get()
        user.ensure_deleted()
        
        uav = Uav.create(
            user_id=user.id,
            model=model,
            serial_number=serial_number,
            reference_number=reference_number,
            noise_characteristics=noise_characteristics,
        )
        await self._uav_gateway.add(uav)
        
        await self._commitable.commit()
