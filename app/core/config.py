# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AgainBuilders"
    database_url: str = "sqlite:///./AgainBuilders.db"  # ✅ This is what Alembic needs
    secret_key: str = "supersecretkey"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 80

    class Config:
        env_file = ".env"  # load variables from .env file
        env_file_encoding = "utf-8"
        extra = "ignore"
settings = Settings()


