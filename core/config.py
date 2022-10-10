from pydantic import BaseSettings

from decouple import config

class Settings(BaseSettings):
    # project name
    PROJECT_NAME : str = config("PROJECT_NAME" , cast=str)

    # init mongo database
    DATABASE_URL: str = config("DATABASE_URL" , cast=str)
    MONGO_INITDB_DATABASE: str = config("MONGO_INITDB_DATABASE" , cast=str)

    JWT_PUBLIC_KEY: str = config("JWT_PUBLIC_KEY" , cast=str)
    JWT_PRIVATE_KEY: str = config("JWT_PRIVATE_KEY" , cast=str)
    REFRESH_TOKEN_EXPIRES_IN: int = config("REFRESH_TOKEN_EXPIRES_IN" , cast=int)
    ACCESS_TOKEN_EXPIRES_IN: int = config("ACCESS_TOKEN_EXPIRES_IN" , cast=int)
    JWT_ALGORITHM: str = config("JWT_ALGORITHM" , cast=str)

    CLIENT_ORIGIN: str = config("CLIENT_ORIGIN" , cast=str)

    class Config:
        case_sensitive = True


settings = Settings()