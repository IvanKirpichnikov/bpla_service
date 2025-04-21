from datetime import datetime


class UavTimeData:
    def __init__(
        self,
        created_at: datetime,
        deleted_at: datetime | None,
    ) -> None:
        self._created_at = created_at
        self._deleted_at = deleted_at
    
    def __repr__(self) -> str:
        return f"UavTimeData(created_at={self._created_at}, deleted_at={self._deleted_at})"
    
    @property
    def created_at(self) -> datetime:
        return self._created_at
    
    @property
    def deleted_at(self) -> datetime | None:
        return self._deleted_at
    
    @property
    def is_deleted(self) -> bool:
        return self._deleted_at is not None
