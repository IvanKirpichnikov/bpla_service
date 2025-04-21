from datetime import datetime, UTC
from typing import Self
from uuid import UUID, uuid4

from bpla_service.domain.uav_flight.enums.status_type import UavFlightStatusType
from bpla_service.domain.uav_flight.value_objects.time_data import UavFlightTimeData

class UavFlight:
    def __init__(
        self,
        id: UUID,
        uav_id: UUID,
        user_id: UUID,
        location: str,
        status: UavFlightStatusType,
        time_data: UavFlightTimeData,
    ) -> None:
        self._id = id
        self._uav_id = uav_id
        self._location = location
        self._status = status
        self._user_id = user_id
        self._time_data = time_data
    
    @classmethod
    def create(
        cls,
        uav_id: UUID,
        user_id: UUID,
        location: str,
        start_at: datetime,
        end_at: datetime,
    ) -> Self:
        return cls(
            id=uuid4(),
            uav_id=uav_id,
            user_id=user_id,
            location=location,
            status=UavFlightStatusType.UNDER_REVIEW,
            time_data=UavFlightTimeData(
                start_at=start_at,
                end_at=end_at,
                created_at=datetime.now(tz=UTC),
                deleted_at=None,
            ),
        )
    
    @property
    def id(self) -> UUID:
        return self._id
    
    @property
    def uav_id(self) -> UUID:
        return self._uav_id
    
    @property
    def location(self) -> str:
        return self._location
    
    @property
    def user_id(self) -> UUID:
        return self._user_id
    
    @property
    def status(self) -> UavFlightStatusType:
        return self._status
    
    @property
    def time_data(self) -> UavFlightTimeData:
        return self._time_data
