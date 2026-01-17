import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "20807000"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "cde2366a7c61e23f4cb44618cbe6cf70")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8564398983:AAHuuntq53gVgwIxQash63fatvHq-27BJTc")

OWNER_ID = int(os.environ.get("OWNER_ID", "890749443"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "5938871512").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://princepia161_db_user:KZWhQUyEe59dF1jh@cluster0.uhoxe0h.mongodb.net/?appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003646612944"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
