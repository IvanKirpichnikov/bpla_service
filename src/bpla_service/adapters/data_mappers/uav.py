from typing import Iterable, override
from uuid import UUID

from sqlalchemy import insert, RowMapping, select
from sqlalchemy.ext.asyncio import AsyncSession

from bpla_service.adapters.data_mappers.tables import uav
from bpla_service.adapters.identity_map import IdentityMap
from bpla_service.application.uav.gateway import UavGateway, UavsGateway
from bpla_service.domain.uav.entity import Uav
from bpla_service.domain.uav.value_objects.characteristics import UavCharacteristics
from bpla_service.domain.uav.value_objects.time_data import UavTimeData
from bpla_service.domain.uav.value_objects.uav_data import UavData


def _load_entity(row: RowMapping) -> Uav:
    return Uav(
        id=row["id"],
        user_id=row["user_id"],
        data=UavData(
            model=row["model"],
            serial_number=row["serial_number"],
            reference_number=row["reference_number"],
        ),
        time_data=UavTimeData(
            created_at=row["created_at"],
            deleted_at=row["deleted_at"],
        ),
        characteristics=UavCharacteristics(
            noise_characteristics=row["noise_characteristics"],
        ),
    )


class UavDataMapper(UavGateway):
    def __init__(
        self,
        session: AsyncSession,
        identity_map: IdentityMap[Uav],
    ) -> None:
        self._session = session
        self._identity_map = identity_map
    
    @override
    async def add(self, entity: Uav) -> None:
        stmt = insert(uav).values(
            id=entity.id,
            user_id=entity.user_id,
            model=entity.data.model,
            serial_number=entity.data.serial_number,
            created_at=entity.time_data.created_at,
            deleted_at=entity.time_data.deleted_at,
            reference_number=entity.data.reference_number,
            noise_characteristics=entity.characteristics.noise_characteristics,
        )
        await self._session.execute(stmt)
        self._identity_map.set(Uav, entity.id, entity)
    
    @override
    async def update(self, entity: Uav) -> None:
        stmt = insert(uav).values(
            id=entity.id,
            user_id=entity.user_id,
            model=entity.data.model,
            serial_number=entity.data.serial_number,
            created_at=entity.time_data.created_at,
            deleted_at=entity.time_data.deleted_at,
            reference_number=entity.data.reference_number,
            noise_characteristics=entity.characteristics.noise_characteristics,
        )
        await self._session.execute(stmt)
        self._identity_map.set(Uav, entity.id, entity)
    
    @override
    async def with_id(self, id: UUID) -> Uav:
        cache_entity = self._identity_map.get(Uav, id)
        if cache_entity:
            return cache_entity
        
        stmt = select(uav).where(uav.c.id == id)
        result = await self._session.execute(stmt)
        row = result.mappings().fetchone()
        if row is None:
            raise ValueError(f"Uav with id {id} not found")
        
        entity = _load_entity(row)
        self._identity_map.set(Uav, entity.id, entity)
        return entity


class UavsDataMapper(UavsGateway):
    def __init__(
        self,
        session: AsyncSession,
        identity_map: IdentityMap[Uav],
    ) -> None:
        self._session = session
        self._identity_map = identity_map
    
    async def with_user_id(self, user_id: UUID) -> Iterable[Uav]:
        stmt = select(uav).where(uav.c.user_id == user_id)
        result = await self._session.execute(stmt)
        entities = []
        for row in result.mappings().all():
            entity = _load_entity(row)
            self._identity_map.set(Uav, entity.id, entity)
            entities.append(entity)
            
        return entities
