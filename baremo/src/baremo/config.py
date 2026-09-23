"""Configuración única del proyecto, leída de variables de entorno y de `.env`.

Regla: ningún otro módulo lee `os.environ` directamente; todos usan `obtener_config()`.
"""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="BAREMO_", extra="ignore")

    modelo_principal: str = "claude-opus-5"
    modelo_extraccion: str = "claude-opus-5"
    dir_datos: Path = Path("data")
    db: Path = Path("data/baremo.duckdb")
    pausa_descarga_s: float = 2.0


@lru_cache(maxsize=1)
def obtener_config() -> Config:
    return Config()
