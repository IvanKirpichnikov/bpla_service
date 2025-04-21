import json
from typing import Final

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import Response

from bpla_service.application.user.interactors.auth import AuthUser
from bpla_service.config import SessionConfig
from bpla_service.domain.user.errors import (
    UserDeletedError,
    UserEmailNotValidError,
    UserNotFoundError,
    UserPasswordNotValidError,
)


router = APIRouter(route_class=DishkaRoute)
USER_NOT_FOUND_RESPONSE: Final = Response(
    status_code=404,
    content=json.dumps({"error": "User not found"}),
)
USER_PASSWORD_NOT_VALID_RESPONSE: Final = Response(
    status_code=400,
    content=json.dumps({"error": "User password not valid"})
)
USER_DELETED_RESPONSE: Final = Response(
    status_code=400,
    content=json.dumps({"error": "User deleted"}),
)
USER_EMAIL_NOT_VALID_RESPONSE: Final = Response(
    status_code=400,
    content=json.dumps({"error": "User email not valid"}),
)


class AuthSchema(BaseModel):
    email: str
    password: str


@router.post('/api/auth')
async def auth(
    schema: AuthSchema,
    config: FromDishka[SessionConfig],
    interactor: FromDishka[AuthUser],
) -> Response:
    try:
        encrypted_session_id = await interactor(
            email=schema.email,
            password=schema.password,
        )
    except UserEmailNotValidError:
        return USER_EMAIL_NOT_VALID_RESPONSE
    except UserNotFoundError:
        return USER_NOT_FOUND_RESPONSE
    except UserDeletedError:
        return USER_DELETED_RESPONSE
    except UserPasswordNotValidError:
        return USER_PASSWORD_NOT_VALID_RESPONSE

    response = Response(status_code=200)
    response.set_cookie(
        key=config.cookie_key,
        value=encrypted_session_id,
        httponly=True,
    )
    return response
