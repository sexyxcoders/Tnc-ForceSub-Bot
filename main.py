from Tnc import *
import asyncio
import logging
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from Tnc import LOG

logging.basicConfig(level=logging.INFO)

app = Client(
    "TncForceJoinBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Import all plugin handlers
from plugins import start, core, invite, ownercmds  # noqa: F401

async def main():
    LOG.info("🚀 Tnc Force Join Bot v6 is starting...")
    await app.start()
    LOG.info("✅ Bot is online and running successfully.")
    await idle()  # Keeps the bot alive
    LOG.info("🛑 Bot stopped manually.")
    await app.stop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        LOG.info("❌ Bot stopped due to system exit or interrupt.")