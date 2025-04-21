from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import Response

from bpla_service.application.user.interactors.logout import Logout
from bpla_service.config import SessionConfig


router = APIRouter(route_class=DishkaRoute)


@router.post('/api/logout')
async def logout(
    request: Request,
    interactor: FromDishka[Logout],
    config: FromDishka[SessionConfig],
) -> Response:
    await interactor()
    response = Response(status_code=200)
    response.delete_cookie(key=config.cookie_key)
    return response
