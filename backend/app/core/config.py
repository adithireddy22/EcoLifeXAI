import os
from pathlib import Path

from dotenv import load_dotenv

# Locate the backend directory
BACKEND_DIR = Path(__file__).resolve().parents[2]

# Load environment variables from backend/.env
ENV_FILE = BACKEND_DIR / ".env"
load_dotenv(ENV_FILE)

# Application settings
APP_NAME = os.getenv("APP_NAME", "EcoLifeXAI")
APP_ENV = os.getenv("APP_ENV", "development")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"