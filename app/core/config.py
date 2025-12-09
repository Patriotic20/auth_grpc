from pydantic import BaseModel, PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerConfig(BaseModel):
    host: str
    port: int


class DataBaseConfig(BaseModel):
    user: str
    password: str
    db: str
    host: str = "postgres"
    port: int = 5432

    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    @computed_field
    @property
    def url(self) -> PostgresDsn:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    server: ServerConfig
    db: DataBaseConfig


settings = AppConfig()