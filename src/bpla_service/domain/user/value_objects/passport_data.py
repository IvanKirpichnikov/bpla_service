from datetime import datetime

from bpla_service.domain.user.enums.gender_type import UserGenderType


class PassportData:
    def __init__(
        self,
        fio: str,
        issued_by: str,
        date_of_issue: datetime,
        subdivision_code: str,
        gender: UserGenderType,
        year_of_birth: datetime,
        place_of_birth: str,
        serial_number: str,
        number: str,
        snils: str
    ) -> None:
        self._fio = fio
        self._issued_by = issued_by
        self._date_of_issue = date_of_issue
        self._subdivision_code = subdivision_code
        self._gender = gender
        self._year_of_birth = year_of_birth
        self._place_of_birth = place_of_birth
        self._serial_number = serial_number
        self._number = number
        self._snils = snils
    
    @property
    def fio(self) -> str:
        return self._fio
    
    @property
    def issued_by(self) -> str:
        return self._issued_by
    
    @property
    def date_of_issue(self) -> datetime:
        return self._date_of_issue
    
    @property
    def subdivision_code(self) -> str:
        return self._subdivision_code
    
    @property
    def gender(self) -> UserGenderType:
        return self._gender
    
    @property
    def year_of_birth(self) -> datetime:
        return self._year_of_birth
    
    @property
    def place_of_birth(self) -> str:
        return self._place_of_birth
    
    @property
    def serial_number(self) -> str:
        return self._serial_number
    
    @property
    def number(self) -> str:
        return self._number
    
    @property
    def snils(self) -> str:
        return self._snils
