from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

class Settings(BaseSettings):
    server_host: str = "localhost"
    server_port: int = 8000
    db_server: str = DB_HOST
    db_port: int = DB_PORT
    db_name: str = DB_NAME
    db_user: str = DB_USER
    db_password: str = DB_PASS
    db_url: str = f"postgresql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}"
    jwt_secret: str = 'VB4bN97doJGMOe-GiVZ0qcH9Lj0D2kiTp8I0aovLP0k'
    jwt_algoritm: str = "HS256"
    jwt_expiation: int = 3600

settings = Settings(
    _env_file='.env-non-dev',
    _env_file_encoding='utf-8',
)
