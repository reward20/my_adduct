from pathlib import Path

from pydantic import PostgresDsn, SecretStr, PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

__all__ = [
    "setting",
    "db_engine",
    "db_session",
    "templating",
    "static",
]

from fastapi.staticfiles import StaticFiles

from starlette.templating import Jinja2Templates


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env"
    )

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    POSTGRES_URL: PostgresDsn
    GOOGLE_CLIENT_ID: SecretStr
    GOOGLE_CLIENT_TOKEN: SecretStr
    GOOGLE_SCOPES: list[str]


setting = Setting()
db_engine = create_async_engine(url=setting.POSTGRES_URL.unicode_string())
db_session = async_sessionmaker(bind=db_engine)
templating = Jinja2Templates(directory=setting.BASE_DIR / "templates")
static = StaticFiles(directory=setting.BASE_DIR / "static")
