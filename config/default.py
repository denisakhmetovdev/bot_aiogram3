from os import getenv
from dotenv import load_dotenv
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parent.parent
dotenv_path = Path(ROOT_DIR, "config", ".env")

load_dotenv(dotenv_path)


class Settings(BaseSettings):
    TOKEN: str

    @property
    def bot_token(self):
        token = getenv("BOT_TOKEN")
        return token

    model_config = SettingsConfigDict(env_file=Path(ROOT_DIR, "config", '.env'))


settings = Settings()
