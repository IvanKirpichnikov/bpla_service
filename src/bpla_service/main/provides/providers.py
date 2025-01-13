from dishka import provide, Provider as DishkaProvider, Scope

from uav_service.application.provider import Provider
from uav_service.domain.session.entity import Session
from uav_service.domain.user.entity import User
from uav_service.adapters.providers import SessionProvider, UserProvider


class ProviderProvider(DishkaProvider):
    scope = Scope.REQUEST
    
    user_provider = provide(
        UserProvider,
        provides=Provider[User],
    )
    session_provider = provide(
        SessionProvider,
        provides=Provider[Session],
    )
