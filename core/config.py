from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunSettings(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000


class ApiSettings(BaseModel):
    prefix: str = '/api'


class DatabaseSettings(BaseModel):
    url: PostgresDsn 
    echo: bool = False
    echo_pull: bool = False
    poll_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        case_sensitive=False,
        env_nested_delimiter='__',
        env_prefix='APP_CONFIG__', 
    )

    run: RunSettings = RunSettings()
    api: ApiSettings = ApiSettings()
    db: DatabaseSettings


settings = Settings()

