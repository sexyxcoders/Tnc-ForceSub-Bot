from Tnc import *
import os

API_ID = int(os.getenv("API_ID", "12345"))
API_HASH = os.getenv("API_HASH", "your_api_hash_here")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")
MONGO_URL = os.getenv("MONGO_URL", "your_mongodb_connection_string_here")

START_IMAGE = "assets/start.jpg"
BOT_NAME = "Tnc Must Join Bot"
SUPPORT_CHAT = "https://t.me/TncSupport"
FORCE_CHANNEL = "@TechNodeCoders"

OWNER_ID = 8487284125
