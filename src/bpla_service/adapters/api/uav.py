from datetime import datetime
from decimal import Decimal
from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import Response

from bpla_service.application.uav.interactors.add import AddUav
from bpla_service.application.uav.interactors.read import ReadUav
from bpla_service.application.uav.interactors.read_all import ReadAllUavs


router = APIRouter(route_class=DishkaRoute)


class AddUavSchema(BaseModel):
    model: str
    serial_number: str
    reference_number: str
    noise_characteristics: Decimal


@router.post('/api/uav')
async def add_uav(
    schema: AddUavSchema,
    interactor: FromDishka[AddUav],
) -> Response:
    await interactor(
        model=schema.model,
        serial_number=schema.serial_number,
        reference_number=schema.reference_number,
        noise_characteristics=schema.noise_characteristics,
    )
    return Response(status_code=200)


class UavSchema(BaseModel):
    id: UUID
    model: str
    serial_number: str
    created_at: datetime
    noise_characteristics: Decimal
    reference_number: str
    


class UavsSchema(BaseModel):
    uavs: list[UavSchema]


@router.get('/api/uavs')
async def get_uavs(
    interactor: FromDishka[ReadAllUavs],
) -> UavsSchema:
    uavs = await interactor()
    return UavsSchema(
        uavs=[
            UavSchema(
                id=uav.id,
                model=uav.model,
                created_at=uav.created_at,
                serial_number=uav.serial_number,
                reference_number=uav.reference_number,
                noise_characteristics=uav.noise_characteristics,
            )
            for uav in uavs
        ],
    )


@router.get('/api/uav/{uav_id}')
async def get_uav(
    uav_id: UUID,
    interactor: FromDishka[ReadUav],
) -> UavSchema:
    uav = await interactor(uav_id)
    return UavSchema(
        id=uav.id,
        model=uav.model,
        created_at=uav.created_at,
        serial_number=uav.serial_number,
        reference_number=uav.reference_number,
        noise_characteristics=uav.noise_characteristics,
    )
