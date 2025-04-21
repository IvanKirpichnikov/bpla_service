from typing import override
from uuid import UUID

from sqlalchemy import insert, RowMapping, select
from sqlalchemy.ext.asyncio import AsyncSession

from bpla_service.adapters.data_mappers.tables import users
from bpla_service.adapters.identity_map import IdentityMap
from bpla_service.application.user.gateway import UserGateway
from bpla_service.domain.user.entity import User
from bpla_service.domain.user.enums.gender_type import UserGenderType
from bpla_service.domain.user.errors import UserNotFoundError
from bpla_service.domain.user.value_objects.passport_data import PassportData
from bpla_service.domain.user.value_objects.time_data import UserTimeData


def _load_entity(data: RowMapping) -> User:
    return User(
        id=data["id"],
        email=data["email"],
        hashed_password=data["hashed_password"],
        time_data=UserTimeData(
            created_at=data["created_at"],
            deleted_at=data["deleted_at"],
        ),
        passport_data=PassportData(
            fio=data['fio'],
            issued_by=data["issued_by"],
            date_of_issue=data["date_of_issue"],
            subdivision_code=data["subdivision_code"],
            gender=UserGenderType(data["gender"]),
            year_of_birth=data["year_of_birth"],
            place_of_birth=data["place_of_birth"],
            serial_number=data["serial_number"],
            number=data["number"],
            snils=data["snils"],
        ),
    )


class UserDataMapper(UserGateway):
    def __init__(
        self,
        session: AsyncSession,
        identity_map: IdentityMap[User],
    ) -> None:
        self._session = session
        self._identity_map = identity_map
    
    @override
    async def add(self, entity: User) -> None:
        stmt = insert(users).values(
            id=entity.id,
            email=entity.email,
            hashed_password=entity.hashed_password,
            created_at=entity.time_data.created_at,
            deleted_at=entity.time_data.deleted_at,
            issued_by=entity.passport_data.issued_by,
            date_of_issue=entity.passport_data.date_of_issue,
            subdivision_code=entity.passport_data.subdivision_code,
            gender=entity.passport_data.gender.value,
            year_of_birth=entity.passport_data.year_of_birth,
            place_of_birth=entity.passport_data.place_of_birth,
            serial_number=entity.passport_data.serial_number,
            number=entity.passport_data.number,
            snils=entity.passport_data.snils,
            fio=entity.passport_data.fio,
        )
        await self._session.execute(stmt)
        self._identity_map.set(User, entity.id, entity)
    
    @override
    async def with_id(self, id: UUID) -> User:
        cache_entity = self._identity_map.get(User, id)
        if cache_entity:
            return cache_entity
        
        stmt = select(users).where(users.c.id == id)
        result = await self._session.execute(stmt)
        row = result.mappings().fetchone()
        if row is None:
            raise ValueError(f"User with id {id} not found")
        
        entity = _load_entity(row)
        self._identity_map.set(User, id, entity)
        return entity
    
    @override
    async def with_email(self, email: str) -> User:
        stmt = select(users).where(users.c.email == email)
        result = await self._session.execute(stmt)
        row = result.mappings().fetchone()
        if row is None:
            raise UserNotFoundError(f"User with email {email} not found")
        
        entity = _load_entity(row)
        self._identity_map.set(User, entity.id, entity)
        return entity
    
    @override
    async def update(self, entity: User) -> None:
        stmt = insert(users).values(
            id=entity.id,
            email=entity.email,
            hashed_password=entity.hashed_password,
            created_at=entity.time_data.created_at,
            deleted_at=entity.time_data.deleted_at,
            issued_by=entity.passport_data.issued_by,
            date_of_issue=entity.passport_data.date_of_issue,
            subdivision_code=entity.passport_data.subdivision_code,
            gender=entity.passport_data.gender,
            year_of_birth=entity.passport_data.year_of_birth,
            place_of_birth=entity.passport_data.place_of_birth,
            serial_number=entity.passport_data.serial_number,
            number=entity.passport_data.number,
            snils=entity.passport_data.snils,
            fio=entity.passport_data.fio,
        )
        await self._session.execute(stmt)
        self._identity_map.set(User, entity.id, entity)
