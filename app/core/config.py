from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache

class Settings(BaseSettings):
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Efiko API"
    
    # Security
    GEMINI_API_KEY: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    BACKEND_CORS_ORIGINS: list = ["*"]
    
    # File Upload
    MAX_FILE_SIZE: int = 15 * 1024 * 1024  # 15MB
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
