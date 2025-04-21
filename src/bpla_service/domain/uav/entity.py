from __future__ import annotations

from datetime import datetime, UTC
from decimal import Decimal
from uuid import UUID, uuid4

from bpla_service.domain.uav.value_objects.characteristics import UavCharacteristics
from bpla_service.domain.uav.value_objects.time_data import UavTimeData
from bpla_service.domain.uav.value_objects.uav_data import UavData


class Uav:
    def __init__(
        self,
        id: UUID,
        user_id: UUID,
        data: UavData,
        time_data: UavTimeData,
        characteristics: UavCharacteristics,
    ) -> None:
        self._id = id
        self._user_id = user_id
        self._data = data
        self._characteristics = characteristics
        self._time_data = time_data
    
    @property
    def id(self) -> UUID:
        return self._id
    
    @property
    def user_id(self) -> UUID:
        return self._user_id
    
    @property
    def data(self) -> UavData:
        return self._data
    
    @property
    def characteristics(self) -> UavCharacteristics:
        return self._characteristics
    
    @property
    def time_data(self) -> UavTimeData:
        return self._time_data
    
    @classmethod
    def create(
        cls,
        user_id: UUID,
        model: str,
        serial_number: str,
        reference_number: str,
        noise_characteristics: Decimal,
    ) -> Uav:
        return cls(
            id=uuid4(),
            user_id=user_id,
            data=UavData(
                model=model,
                serial_number=serial_number,
                reference_number=reference_number
            ),
            time_data=UavTimeData(
                created_at=datetime.now(tz=UTC),
                deleted_at=None,
            ),
            characteristics=UavCharacteristics(
                noise_characteristics=noise_characteristics,
            ),
        )
