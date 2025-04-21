from dishka import provide_all, Provider, Scope

from bpla_service.application.uav.interactors.add import AddUav
from bpla_service.application.uav.interactors.read import ReadUav
from bpla_service.application.uav.interactors.read_all import ReadAllUavs
from bpla_service.application.uav_flight.interactors.add import AddUavFlight
from bpla_service.application.uav_flight.interactors.read import ReadUavFlight
from bpla_service.application.uav_flight.interactors.read_all import ReadUavFlights
from bpla_service.application.user.interactors.auth import AuthUser
from bpla_service.application.user.interactors.get_me import GetMe
from bpla_service.application.user.interactors.login import LoginUser
from bpla_service.application.user.interactors.logout import Logout


class InteractorProvider(Provider):
    scope = Scope.REQUEST
    
    interactors = provide_all(
        AuthUser,
        LoginUser,
        GetMe,
        Logout,
        AddUav,
        ReadUav,
        ReadAllUavs,
        ReadUavFlight,
        ReadUavFlights,
        AddUavFlight,
    )
    