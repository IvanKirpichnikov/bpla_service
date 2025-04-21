from bpla_service.domain.errors import DomainError


class UserDeletedError(DomainError):
    pass

class UserNotFoundError(DomainError):
    pass


class UserAlreadyExistsError(DomainError):
    pass

class UserEmailNotValidError(DomainError):
    pass

class UserPasswordNotValidError(DomainError):
    pass