from dishka import AsyncContainer, make_async_container
from dishka.integrations.starlette import StarletteProvider

from uav_service.config import Config
from uav_service.main.provides.config import ConfigProvider
from uav_service.main.provides.connection import ConnectionProvider
from uav_service.main.provides.context import ContextProvider
from uav_service.main.provides.cryptographer import CryptographerProvider
from uav_service.main.provides.data_mapper import DataMapperProvider
from uav_service.main.provides.interactor import InteractorProvider
from uav_service.main.provides.providers import ProviderProvider


def build_container(
    config: Config,
) -> AsyncContainer:
    container = make_async_container(
        ConfigProvider(),
        ContextProvider(),
        ProviderProvider(),
        StarletteProvider(),
        ConnectionProvider(),
        DataMapperProvider(),
        InteractorProvider(),
        CryptographerProvider(),
        context={Config: config},
    )
    return container
