"""Configuración única del proyecto, leída de variables de entorno y de `.env`.

Regla: ningún otro módulo lee `os.environ` directamente; todos usan `obtener_config()`.
"""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="CC_", extra="ignore")

    modelo_principal: str = "claude-opus-5"
    modelo_extraccion: str = "claude-opus-5"
    declarenta_cmd: str = "node vendor/declarenta/dist/cli.js"
    dir_datos: Path = Path("data")


@lru_cache(maxsize=1)
def obtener_config() -> Config:
    return Config()
