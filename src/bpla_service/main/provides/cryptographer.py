import argon2
from cryptography.fernet import Fernet
from dishka import provide, Provider, Scope

from bpla_service.application.session.cryptographer import SessionCryptographer
from bpla_service.application.user.password_hasher import PasswordHasher
from bpla_service.config import CryptographerConfig


class CryptographerProvider(Provider):
    scope = Scope.APP
    
    @provide
    def password_hasher(self) -> PasswordHasher:
        return PasswordHasher(argon2.PasswordHasher())
    
    @provide
    def session_cryptographer(self, config: CryptographerConfig) -> SessionCryptographer:
        return SessionCryptographer(Fernet(config.session_key))
