import json
from datetime import datetime
from typing import Final

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import RedirectResponse, Response

from bpla_service.application.user.interactors.login import LoginUser, PassportDataDs
from bpla_service.config import SessionConfig
from bpla_service.domain.user.enums.gender_type import UserGenderType
from bpla_service.domain.user.errors import UserAlreadyExistsError, UserEmailNotValidError


router = APIRouter(route_class=DishkaRoute)
EMAIL_NOT_VALID_RESPONSE: Final = Response(
    status_code=400,
    content=json.dumps({"error": "User email not valid"}),
)
USER_ALREADY_EXISTS_RESPONSE: Final = RedirectResponse(url="/auth")

class PassportDataSchema(BaseModel):
    issued_by: str
    date_of_issue: datetime
    subdivision_code: str
    gender: UserGenderType
    year_of_birth: datetime
    place_of_birth: str
    serial_number: str
    number: str
    snils: str
    fio: str


class LoginSchema(BaseModel):
    email: str
    password: str
    passport_data: PassportDataSchema


@router.post('/api/login')
async def login_endpoint(
    schema: LoginSchema,
    config: FromDishka[SessionConfig],
    interactor: FromDishka[LoginUser],
) -> Response:
    try:
        session_id = await interactor(
            email=schema.email,
            password=schema.password,
            passport_data=PassportDataDs(
                issued_by=schema.passport_data.issued_by,
                gender=schema.passport_data.gender,
                number=schema.passport_data.number,
                date_of_issue=schema.passport_data.date_of_issue,
                year_of_birth=schema.passport_data.year_of_birth,
                serial_number=schema.passport_data.serial_number,
                place_of_birth=schema.passport_data.place_of_birth,
                subdivision_code=schema.passport_data.subdivision_code,
                snils=schema.passport_data.snils,
                fio=schema.passport_data.fio,
            ),
        )
    except UserEmailNotValidError:
        return EMAIL_NOT_VALID_RESPONSE
    except UserAlreadyExistsError:
        return USER_ALREADY_EXISTS_RESPONSE
    
    response = Response(status_code=200)
    response.set_cookie(
        key=config.cookie_key,
        value=session_id,
        httponly=True,
    )
    return response
