from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    transport: Literal["stdio", "http", "sse", "streamable-http"] = Field(
        "stdio",
        description="The transport to use for the MCP server.",
    )

    port: int = Field(
        8000,
        description="The port to use for the MCP server.",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="MCP_",
    )


@lru_cache()
def get_settings() -> Settings:
    """Get the application settings."""
    return Settings()
