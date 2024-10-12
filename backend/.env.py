import pathlib
from functools import lru_cache

from decouple import Config, RepositoryEnv

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

ENV_PATH = BASE_DIR.parent / ".env"


@lru_cache
def get_config(use_gcloud=True):
    if ENV_PATH.exists():
        return Config(RepositoryEnv(ENV_PATH))
    from decouple import config

    return config


config = get_config()
