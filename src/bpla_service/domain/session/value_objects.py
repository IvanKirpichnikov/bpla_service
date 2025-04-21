from datetime import datetime


class SessionTimeData:
    def __init__(
        self,
        expires_in: datetime,
        created_at: datetime,
        deleted_at: datetime | None = None,
    ) -> None:
        self._expires_in = expires_in
        self._created_at = created_at
        self._deleted_at = deleted_at
    
    def __hash__(self) -> int:
        return hash((self._expires_in, self._created_at, self._deleted_at))
    
    def __repr__(self) -> str:
        return (f"UserTimeData(expires_in={self._expires_in}, created_at={self._created_at}, deleted_at="
                f"{self._deleted_at})")
    
    @property
    def created_at(self) -> datetime:
        return self._created_at
    
    @property
    def expires_in(self) -> datetime:
        return self._expires_in
    
    @property
    def deleted_at(self) -> datetime | None:
        return self._deleted_at
    
    @deleted_at.setter
    def deleted_at(self, value: datetime) -> None:
        if value < self._created_at:
            raise ValueError(
                "deleted_at(%r) must be greater than created_at(%r)" % (value, self._created_at),
            )
        self._deleted_at = value
