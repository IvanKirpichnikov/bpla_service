from typing import override
from uuid import UUID

from sqlalchemy import insert, RowMapping, select
from sqlalchemy.ext.asyncio import AsyncSession

from bpla_service.adapters.data_mappers.tables import uav_flight
from bpla_service.adapters.identity_map import IdentityMap
from bpla_service.application.uav_flight.gateway import UavFlightGateway, UavFlightsGateway
from bpla_service.domain.uav_flight.entity import UavFlight
from bpla_service.domain.uav_flight.value_objects.time_data import UavFlightTimeData


def _load_entity(row: RowMapping) -> UavFlight:
    return UavFlight(
        id=row["id"],
        uav_id=row["uav_id"],
        user_id=row["user_id"],
        status=row["status"],
        location=row["location"],
        time_data=UavFlightTimeData(
            start_at=row["start_at"],
            end_at=row["end_at"],
            created_at=row["created_at"],
            deleted_at=row["deleted_at"],
        ),
    )


class UavFlightDataMapper(UavFlightGateway):
    def __init__(
        self,
        session: AsyncSession,
        identity_map: IdentityMap[UavFlight],
    ) -> None:
        self._session = session
        self._identity_map = identity_map
    
    @override
    async def add(self, entity: UavFlight) -> None:
        stmt = insert(uav_flight).values(
            id=entity.id,
            user_id=entity.user_id,
            uav_id=entity.uav_id,
            location=entity.location,
            status=entity.status.value,
            start_at=entity.time_data.start_at,
            end_at=entity.time_data.end_at,
            created_at=entity.time_data.created_at,
            deleted_at=entity.time_data.deleted_at,
        )
        await self._session.execute(stmt)
        self._identity_map.set(UavFlight, entity.id, entity)
    
    @override
    async def update(self, entity: UavFlight) -> None:
        stmt = insert(uav_flight).values(
            id=entity.id,
            user_id=entity.user_id,
            uav_id=entity.uav_id,
            location=entity.location,
            status=entity.status.value,
            start_at=entity.time_data.start_at,
            end_at=entity.time_data.end_at,
            created_at=entity.time_data.created_at,
            deleted_at=entity.time_data.deleted_at,
        )
        await self._session.execute(stmt)
        self._identity_map.set(UavFlight, entity.id, entity)
    
    @override
    async def with_id(self, id: UUID) -> UavFlight:
        cache_entity = self._identity_map.get(UavFlight, id)
        if cache_entity:
            return cache_entity
        
        stmt = select(uav_flight).where(uav_flight.c.id == id)
        result = await self._session.execute(stmt)
        row = result.mappings().fetchone()
        if row is None:
            raise ValueError(f"UavFlight with id {id} not found")
        
        entity = _load_entity(row)
        self._identity_map.set(UavFlight, entity.id, entity)
        return entity

class UavFlightsDataMapper(UavFlightsGateway):
    def __init__(
        self,
        session: AsyncSession,
        identity_map: IdentityMap[UavFlight],
    ) -> None:
        self._session = session
        self._identity_map = identity_map
    
    @override
    async def with_user_id(self, user_id: UUID) -> list[UavFlight]:
        stmt = select(uav_flight).where(uav_flight.c.user_id == user_id)
        result = await self._session.execute(stmt)
        
        entities = []
        for row in result.mappings().all():
            entity = _load_entity(row)
            self._identity_map.set(UavFlight, entity.id, entity)
            entities.append(entity)
            
        return entities
    
