from .jwt import JWT
from .password_man import PasswordManager
from sch_link.setting import setting

jwt = JWT(
    access_secret_key=setting.JWT_ACCESS_SECRET_KEY.get_secret_value(),
    access_exp=setting.JWT_ACCESS_EXP,
    access_algorithm=setting.JWT_ACCESS_ALGORITHM,
    refresh_secret_key=setting.JWT_REFRESH_SECRET_KEY.get_secret_value(),
    refresh_exp=setting.JWT_REFRESH_EXP,
    refresh_algorithm=setting.JWT_REFRESH_ALGORITHM
)

__all__ = [
    "jwt",
    "PasswordManager",
]
