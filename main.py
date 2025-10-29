from Tnc import *
import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from Tnc import LOG

app = Client(
    "TncForceJoinBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# load plugins
from plugins import start, core, invite, ownercmds  # noqa: F401

if __name__ == "__main__":
    LOG.info("🚀 Tnc Force Join Bot v5 is starting...")
    app.run()
