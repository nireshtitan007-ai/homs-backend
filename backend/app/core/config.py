import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str = os.getenv("MONGODB_URI", "mongodb://localhost:27017/homs")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "homs")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "7a8b9c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    # SMTP Configuration for Nodemailer-like alerts
    SMTP_HOST: str = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER: str = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")  # Secure Google App Password
    EMAIL_FROM: str = os.getenv("EMAIL_FROM", "homs-alerts@college.edu")

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
