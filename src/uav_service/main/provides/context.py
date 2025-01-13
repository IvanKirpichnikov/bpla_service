from dishka import from_context, Provider, Scope

from uav_service.config import Config


class ContextProvider(Provider):
    scope = Scope.APP
    
    config = from_context(Config)
