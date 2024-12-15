from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    
    
class DataBaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool=False, 
    echo_pool: bool = False,
    pool_size: int = 50,
    max_overflow: int = 10    

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        ev_prefix="APP_CONFIG__"
    )
    run: RunConfig = RunConfig()
    db: DataBaseConfig

settings = Settings()