from pydantic import BaseModel
from pydantic-settings import BaseSettings

class RunSettings(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000


class ApiSettings(BaseModel):
    prefix: api = '/api'


class Settings(BaseSettings):
    run: RunSettings = RunSettings()
    api: str = ApiSettings()
    db_url: str
    api_prefix: str

settings = Settings()
