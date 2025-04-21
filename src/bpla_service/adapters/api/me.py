from datetime import datetime
from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from starlette.requests import Request

from bpla_service.application.user.interactors.get_me import GetMe
from bpla_service.domain.session.errors import SessionIsExpiredError


router = APIRouter(route_class=DishkaRoute)


class MeSchema(BaseModel):
    id: UUID
    fio: str
    email: str
    created_at: datetime


@router.get('/api/me')
async def me(
    request: Request,
    interactor: FromDishka[GetMe],
) -> MeSchema:
    try:
        me_ = await interactor()
    except SessionIsExpiredError:
        raise HTTPException(
            status_code=307,
            detail={'error': 'to login'},
            headers={'Location': '/login'},
        )
    return MeSchema(
        id=me_.id,
        fio=me_.fio,
        email=me_.email,
        created_at=me_.created_at,
    )
