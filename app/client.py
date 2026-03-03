from telethon import TelegramClient
from app.config import Config

def get_client():
    return TelegramClient(
        "userbot_session",
        Config.API_ID,
        Config.API_HASH
    )