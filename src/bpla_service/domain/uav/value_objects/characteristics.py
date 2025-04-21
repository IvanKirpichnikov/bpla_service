from decimal import Decimal


class UavCharacteristics:
    def __init__(
        self,
        noise_characteristics: Decimal,
    ) -> None:
        self._noise_characteristics = noise_characteristics
    
    @property
    def noise_characteristics(self) -> Decimal:
        return self._noise_characteristics
