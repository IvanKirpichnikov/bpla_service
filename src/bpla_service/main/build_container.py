from dishka import AsyncContainer, make_async_container
from dishka.integrations.starlette import StarletteProvider

from bpla_service.config import Config
from bpla_service.main.provides.config import ConfigProvider
from bpla_service.main.provides.connection import ConnectionProvider
from bpla_service.main.provides.context import ContextProvider
from bpla_service.main.provides.cryptographer import CryptographerProvider
from bpla_service.main.provides.data_mapper import DataMapperProvider
from bpla_service.main.provides.interactor import InteractorProvider
from bpla_service.main.provides.providers import ProviderProvider


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
