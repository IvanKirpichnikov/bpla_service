from typing import Any

from dishka import alias, provide, Provider, Scope

from bpla_service.adapters.data_mappers.session import SessionDataMapper
from bpla_service.adapters.data_mappers.uav import UavDataMapper, UavsDataMapper
from bpla_service.adapters.data_mappers.uav_flight import UavFlightDataMapper, UavFlightsDataMapper
from bpla_service.adapters.data_mappers.user import UserDataMapper
from bpla_service.adapters.identity_map import IdentityMap
from bpla_service.application.session.gateway import SessionGateway
from bpla_service.application.uav.gateway import UavGateway, UavsGateway
from bpla_service.application.uav_flight.gateway import UavFlightGateway, UavFlightsGateway
from bpla_service.application.user.gateway import UserGateway


class DataMapperProvider(Provider):
    scope = Scope.REQUEST
    
    identity_map = provide(IdentityMap[Any]) + alias(IdentityMap[Any], provides=IdentityMap)
    data_mappers = (
        provide(
            UserDataMapper,
            provides=UserGateway,
        ) +
        provide(
            SessionDataMapper,
            provides=SessionGateway,
        ) +
        provide(
            UavDataMapper,
            provides=UavGateway,
        ) +
        provide(
            UavsDataMapper,
            provides=UavsGateway,
        ) +
        provide(
            UavFlightDataMapper,
            provides=UavFlightGateway,
        ) +
        provide(
            UavFlightsDataMapper,
            provides=UavFlightsGateway,
        )
    )
