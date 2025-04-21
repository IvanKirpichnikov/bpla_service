from uuid import UUID

from cryptography.fernet import Fernet

from bpla_service.domain.session.entity import Session


class SessionCryptographer:
    def __init__(self, fernet: Fernet) -> None:
        self._fernet = fernet
    
    def crypto(self, session: Session) -> str:
        return self._fernet.encrypt(str(session.id).encode("utf-8")).decode("utf-8")
    
    def decrypto(self, raw_session_id: str) -> UUID:
        return UUID(self._fernet.decrypt(raw_session_id).decode("utf-8"))
