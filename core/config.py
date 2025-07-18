from pydantic import BaseModel, PostgresDsn
from pydantic-settings import BaseSettings

class RunSettings(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000


class ApiSettings(BaseModel):
    prefix: api = '/api'


class DatabaseSettings(BaseModel):
    url: PostgresDsn 
    echo: bool = False
    echo_pull: bool = False
    poll_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    run: RunSettings = RunSettings()
    api: str = ApiSettings()
    db: DatabaseSettings
    db_url: str
    api_prefix: str

settings = Settings()
