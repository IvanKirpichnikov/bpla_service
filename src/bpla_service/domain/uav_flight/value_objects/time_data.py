from datetime import datetime


class UavFlightTimeData:
    def __init__(
        self,
        start_at: datetime,
        end_at: datetime,
        created_at: datetime,
        deleted_at: datetime | None = None,
    ) -> None:
        self._start_at = start_at
        self._end_at = end_at
        self._created_at = created_at
        self._deleted_at = deleted_at
    
    @property
    def start_at(self) -> datetime:
        return self._start_at
    
    @property
    def end_at(self) -> datetime:
        return self._end_at
    
    @property
    def created_at(self) -> datetime:
        return self._created_at
    
    @property
    def deleted_at(self) -> datetime | None:
        return self._deleted_at
    
    def is_deleted(self) -> bool:
        return bool(self._deleted_at)
