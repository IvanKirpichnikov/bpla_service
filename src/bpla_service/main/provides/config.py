from dishka import provide, Provider, Scope

from bpla_service.config import Config, CryptographerConfig, DatabaseConfig, SessionConfig


class ConfigProvider(Provider):
    scope = Scope.APP
    
    @provide
    def database(self, config: Config) -> DatabaseConfig:
        return config.database
    
    @provide
    def cryptographer(self, config: Config) -> CryptographerConfig:
        return config.cryptographer
    
    @provide
    def session(self, config: Config) -> SessionConfig:
        return config.session
