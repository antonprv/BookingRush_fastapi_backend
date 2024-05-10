from datetime import datetime

from pydantic import model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    PW_KEY: str
    PW_ALGORITHM: str

    DATABASE_URL: str = ''

    REDIS_HOST: str
    REDIS_PORT: int

    CORS_URL: str

    CACHE_EXPIRE: int

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str

    # Generate a PostgreSQL connection string and validate it at the same time.
    @model_validator(mode='after')
    def get_database_url(cls, v):
        v.DATABASE_URL = (f'postgresql+asyncpg://'
                          f'{v.DB_USER}:{v.DB_PASS}@'
                          f'{v.DB_HOST}:{v.DB_PORT}/{v.DB_NAME}')
        return v

    class Config:
        env_file = '.env'


settings = Settings()
