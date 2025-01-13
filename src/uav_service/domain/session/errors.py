from uav_service.domain.errors import DomainError


class UnauthorizedError(DomainError):
    pass


class SessionIsExpiredError(DomainError):
    pass
