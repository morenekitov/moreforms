from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = Field(default="development", alias="APP_ENV")
    app_debug: bool = Field(default=True, alias="APP_DEBUG")
    app_host: str = Field(default="0.0.0.0", alias="APP_HOST")
    app_port: int = Field(default=8000, alias="APP_PORT")

    database_url: str = Field(default="sqlite:///./moreforms_dev.db", alias="DATABASE_URL")
    sql_echo: bool = Field(default=False, alias="SQL_ECHO")
    auto_create_schema: bool = Field(default=True, alias="AUTO_CREATE_SCHEMA")

    auth_disabled: bool = Field(default=True, alias="AUTH_DISABLED")
    allowed_emails: str = Field(default="", alias="ALLOWED_EMAILS")
    bootstrap_owner_email: str = Field(default="", alias="BOOTSTRAP_OWNER_EMAIL")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def allowed_email_set(self) -> set[str]:
        if not self.allowed_emails.strip():
            return set()
        return {item.strip().lower() for item in self.allowed_emails.split(",") if item.strip()}


@lru_cache
def get_settings() -> Settings:
    return Settings()
