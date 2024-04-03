from passlib.context import CryptContext

__all__ = [
    "PasswordManager",
]


class PasswordManager(object):
    crypt_man = CryptContext(schemes="bcrypt", deprecated="auto")

    @classmethod
    def hash(cls, password: str) -> str:
        return cls.crypt_man.hash(secret=password)

    @classmethod
    def verify(cls, password: str, password_hash: str) -> bool:
        return cls.crypt_man.verify(secret=password, hash=password_hash)
