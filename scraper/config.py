from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")