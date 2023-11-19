from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    BOT_TOKEN: str

    @property
    def bot_token(self):
        return f"{self.BOT_TOKEN}"

    model_config = SettingsConfigDict(env_file=Path(ROOT_DIR, "config", '.env'))


settings = Settings()

print(settings.bot_token)
