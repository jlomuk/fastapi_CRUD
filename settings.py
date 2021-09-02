from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    host: str = '127.0.0.1'
    port: int = 8080
    db_name: str
    db_user: str
    db_password: str
    db_host: str = '127.0.0.1'
    db_port: int = 5432
    db_url: str = 'postgresql://{0}:{1}@{2}:{3}/{4}'


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf8'
)
