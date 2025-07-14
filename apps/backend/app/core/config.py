from dotenv import load_dotenv
import os
from pathlib import Path

# Load .env file if present
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# === Application Config ===
APP_NAME = "BuddyX"

# === Security ===
SECRET_KEY = os.getenv("SECRET_KEY", "super-insecure-dev-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# === Database ===
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./buddyx.db")

# === Environment ===
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
