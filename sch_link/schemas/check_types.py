from re import compile
from typing import Annotated

from annotated_types import Predicate

__all__ = [
    "PasswordStr",
]

PATTERN = compile(pattern=r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,64}$")


def validate_password(value: str) -> bool:
    return PATTERN.fullmatch(string=value) is not None


PasswordStr = Annotated[str, Predicate(func=validate_password)]
