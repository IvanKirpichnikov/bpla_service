import re

from bpla_service.domain.user.errors import UserEmailNotValidError


_email_re_pattern = re.compile("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$")


def user_email_validator(email: str) -> None:
    if _email_re_pattern.findall(email):
        return
    
    raise UserEmailNotValidError
