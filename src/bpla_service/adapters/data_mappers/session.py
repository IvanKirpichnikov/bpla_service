from typing import override
from uuid import UUID

from sqlalchemy import insert, RowMapping, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from bpla_service.adapters.data_mappers.tables import sessions
from bpla_service.adapters.identity_map import IdentityMap
from bpla_service.application.session.gateway import SessionGateway
from bpla_service.domain.session.entity import Session
from bpla_service.domain.session.value_objects import SessionTimeData


def _load_entity(data: RowMapping) -> Session:
    return Session(
        id=data["id"],
        user_id=data["user_id"],
        revoked=data["revoked"],
        time_data=SessionTimeData(
            expires_in=data["expires_in"],
            created_at=data["created_at"],
            deleted_at=data["deleted_at"],
        )
    )


class SessionDataMapper(SessionGateway):
    def __init__(
        self,
        session: AsyncSession,
        identity_map: IdentityMap[Session],
    ) -> None:
        self._session = session
        self._identity_map = identity_map
    
    @override
    async def add(self, entity: Session) -> None:
        stmt = insert(sessions).values(
            id=entity.id,
            user_id=entity.user_id,
            revoked=entity.revoked,
            expires_in=entity.expires_in,
            created_at=entity.created_at,
            deleted_at=entity.deleted_at,
        )
        await self._session.execute(stmt)
        self._identity_map.set(Session, entity.id, entity)
    
    @override
    async def update(self, entity: Session) -> None:
        stmt = update(sessions).values(
            revoked=entity.revoked,
            expires_in=entity.expires_in,
            created_at=entity.created_at,
            deleted_at=entity.deleted_at,
        ).where(sessions.c.id == entity.id)
        
        await self._session.execute(stmt)
        self._identity_map.set(Session, entity.id, entity)
    
    @override
    async def with_id(self, id: UUID) -> Session:
        cache_entity = self._identity_map.get(Session, id)
        if cache_entity:
            return cache_entity
        
        stmt = select(sessions).where(sessions.c.id == id)
        result = await self._session.execute(stmt)
        row = result.mappings().fetchone()
        if row is None:
            raise ValueError(f"Session with id {id} not found")
        
        entity = _load_entity(row)
        self._identity_map.set(Session, entity.id, entity)
        return entity
    
    @override
    async def with_user_id(
        self,
        user_id: UUID,
        include_deleted: bool,
    ) -> Session:
        stmt = select(sessions).where(sessions.c.id == id)
        
        if not include_deleted:
            stmt.where(sessions.c.deleted_at)
        
        result = await self._session.execute(stmt)
        row = result.mappings().fetchone()
        if row is None:
            raise ValueError(f"Session with id {id} not found")
        
        entity = _load_entity(row)
        self._identity_map.set(Session, entity.id, entity)
        return entity
