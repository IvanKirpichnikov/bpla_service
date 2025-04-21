class UavData:
    def __init__(
        self,
        model: str,
        serial_number: str,
        reference_number: str,
    ) -> None:
        self._model = model
        self._serial_number = serial_number
        self._reference_number = reference_number
    
    @property
    def model(self) -> str:
        return self._model
    
    @property
    def serial_number(self) -> str:
        return self._serial_number
    
    @property
    def reference_number(self) -> str:
        return self._reference_number
