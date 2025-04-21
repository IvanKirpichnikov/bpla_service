from __future__ import annotations

from datetime import datetime, timedelta, UTC
from uuid import UUID, uuid4

from bpla_service.domain.session.errors import SessionIsExpiredError
from bpla_service.domain.session.value_objects import SessionTimeData


class Session:
    def __init__(
        self,
        id: UUID,
        user_id: UUID,
        revoked: bool,
        time_data: SessionTimeData,
    ) -> None:
        self._id = id
        self._user_id = user_id
        self._revoked = revoked
        self._time_data = time_data
    
    def __repr__(self) -> str:
        return (
            f"Session(id={self._id}, revoked={self._revoked}, "
            f"time_data={self._time_data}), user_id={self._user_id})"
        )
    
    @classmethod
    def create(
        cls,
        user_id: UUID,
        expires_in: timedelta,
    ) -> Session:
        created_at = datetime.now(tz=UTC)
        return cls(
            id=uuid4(),
            user_id=user_id,
            revoked=False,
            time_data=SessionTimeData(
                created_at=created_at,
                expires_in=created_at + expires_in,
            ),
        )
    
    @property
    def id(self) -> UUID:
        return self._id
    
    @property
    def user_id(self) -> UUID:
        return self._user_id
    
    @property
    def created_at(self) -> datetime:
        return self._time_data.created_at
    
    @property
    def expires_in(self) -> datetime:
        return self._time_data.expires_in
    
    @property
    def deleted_at(self) -> datetime | None:
        return self._time_data.deleted_at
    
    @property
    def revoked(self) -> bool:
        return self._revoked
    
    def verify(self) -> None:
        if (
            (self._time_data.expires_in < datetime.now(tz=UTC))
            or self._revoked
            or self._time_data.deleted_at
        ):
            raise SessionIsExpiredError(self)
    
    def revoke(self) -> None:
        self._revoked = True
        self._time_data.deleted_at = datetime.now(tz=UTC)
