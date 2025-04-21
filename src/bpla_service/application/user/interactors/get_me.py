from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from bpla_service.application.provider import Provider
from bpla_service.domain.user.entity import User


@dataclass
class Me:
    id: UUID
    fio: str
    email: str
    created_at: datetime


class GetMe:
    def __init__(
        self,
        user_provider: Provider[User],
    ) -> None:
        self._user_provider = user_provider
    
    async def __call__(self) -> Me:
        user = await self._user_provider.get()
        user.ensure_deleted()
        
        return Me(
            id=user.id,
            email=user.email,
            fio=user.passport_data.fio,
            created_at=user.time_data.created_at,
        )
