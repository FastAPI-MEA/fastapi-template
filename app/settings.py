from os import environ

from passlib.context import CryptContext


class Settings:
    APP_TITLE = "App name"
    ALLOWED_HOST = environ.get("ALLOWED_HOST")
    SECRET_KEY = environ.get("SECRET_KEY")
    DEBUG = bool(environ.get("DEBUG"))
    ALLOWED_PORT = int(environ.get("PORT"))
    DB_USER = environ.get("POSTGRES_USER")
    DB_PASSWORD = environ.get("POSTGRES_PASSWORD")
    DB_DB = environ.get("POSTGRES_DB")
    DB_PORT = environ.get("POSTGRES_PORT")
    DB_HOST = environ.get("POSTGRES_HOST")
    DB_URL = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DB}"
    )
    TEST_DB = environ.get("POSTGRES_TEST_DB")
    TEST_DB_URL = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{TEST_DB}"
    )
    ACCESS_TOKEN_EXPIRY_TIME = 60 * 30
    REFRESH_TOKEN_EXPIRY_TIME = 60 * 24 * 365
    PASSWORD_HASHER = CryptContext(schemes=["bcrypt"], deprecated="auto")
    JWT_ALGORITHM = "HS256"
    REDIS_HOST = environ.get("REDIS_HOST", "localhost")
    REDIS_PORT = environ.get("REDIS_PORT", "6379")
    PAGE_SIZE = 50


settings = Settings()