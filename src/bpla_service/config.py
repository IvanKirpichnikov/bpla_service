import tomllib
from dataclasses import dataclass
from datetime import timedelta
from pathlib import Path


@dataclass(frozen=True, slots=True)
class SessionConfig:
    cookie_key: str
    expires_in: timedelta


@dataclass(frozen=True, slots=True)
class CryptographerConfig:
    session_key: str


@dataclass(frozen=True, slots=True)
class DatabaseConfig:
    url: str


@dataclass(frozen=True, slots=True)
class Config:
    session: SessionConfig
    database: DatabaseConfig
    cryptographer: CryptographerConfig


def build_config(path: Path) -> Config:
    with path.open(mode="r") as f:
        toml_config = tomllib.loads(f.read())
    
    return Config(
        session=SessionConfig(
            cookie_key=toml_config["session"]["cookie_key"],
            expires_in=timedelta(seconds=(toml_config["session"]["seconds_expires_in"])),
        ),
        database=DatabaseConfig(
            url=toml_config["database"]["url"],
        ),
        cryptographer=CryptographerConfig(
            session_key=toml_config["cryptographer"]["session_key"],
        ),
    )
