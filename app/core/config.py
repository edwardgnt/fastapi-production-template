from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastAPI Production Template"
    database_url: str = "postgresql://postgres:postgres@db:5432/app_db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
