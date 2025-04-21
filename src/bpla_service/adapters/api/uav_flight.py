from datetime import datetime
from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from pydantic import BaseModel

from bpla_service.application.uav_flight.interactors.add import AddUavFlight
from bpla_service.application.uav_flight.interactors.read import ReadUavFlight
from bpla_service.application.uav_flight.interactors.read_all import ReadUavFlights
from bpla_service.domain.uav_flight.enums.status_type import UavFlightStatusType


router = APIRouter(route_class=DishkaRoute)


class UavFlightSchema(BaseModel):
    id: UUID
    uav_id: UUID
    location: str
    start_at: datetime
    end_at: datetime
    created_at: datetime
    status: UavFlightStatusType


@router.get('/api/uav_flight/{uav_flight_id}')
async def get_uav_flight(
    uav_flight_id: UUID,
    interactor: FromDishka[ReadUavFlight],
) -> UavFlightSchema:
    uav_flight = await interactor(uav_flight_id)
    return UavFlightSchema(
        id=uav_flight.id,
        uav_id=uav_flight.uav_id,
        status=uav_flight.status,
        location=uav_flight.location,
        start_at=uav_flight.start_at,
        end_at=uav_flight.end_at,
        created_at=uav_flight.created_at,
    )


@router.get('/api/uav_flights')
async def get_uav_flights(
    interactor: FromDishka[ReadUavFlights],
) -> list[UavFlightSchema]:
    uav_flights = await interactor()
    return [
        UavFlightSchema(
            id=uav_flight.id,
            uav_id=uav_flight.uav_id,
            status=uav_flight.status,
            location=uav_flight.location,
            start_at=uav_flight.start_at,
            end_at=uav_flight.end_at,
            created_at=uav_flight.created_at,
        )
        for uav_flight in uav_flights
    ]


class UavFlightAdditionSchema(BaseModel):
    uav_id: UUID
    location: str
    start_at: datetime
    end_at: datetime


@router.post('/api/uav_flight')
async def add_uav_flight(
    schema: UavFlightAdditionSchema,
    interactor: FromDishka[AddUavFlight],
) -> None:
    await interactor(
        uav_id=schema.uav_id,
        location=schema.location,
        start_at=schema.start_at,
        end_at=schema.end_at,
    )
