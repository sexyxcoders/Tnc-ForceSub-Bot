from Tnc import *
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import START_IMAGE, BOT_NAME, SUPPORT_CHAT, FORCE_CHANNEL, OWNER_ID
from main import app

@app.on_message(filters.command("start") & filters.private)
async def start_cmd(_, m):
    user = m.from_user
    joined = False
    try:
        member = await app.get_chat_member(FORCE_CHANNEL, user.id)
        if member and getattr(member, "status", None) not in ["left", "kicked"]:
            joined = True
    except Exception:
        joined = False

    if not joined and user.id != OWNER_ID:
        btn = InlineKeyboardMarkup([[InlineKeyboardButton("📢 Join Channel", url="https://t.me/TechNodeCoders")]])
        return await m.reply_text("❌ You must join {} first to use this bot.\n🔗 Join the channel and then press /start again.".format(FORCE_CHANNEL), reply_markup=btn)

    caption = "💫 𝗧𝗡𝗖 𝗠𝗨𝗦𝗧 𝗝𝗢𝗜𝗡 𝗕𝗢𝗧\n👑 Made by ㅤ- 𝖳ɴᴄ //Ｉᴠ ⋏ ᥒ\n🔗 Must Join: {}".format(FORCE_CHANNEL)
    try:
        await app.send_photo(m.chat.id, START_IMAGE, caption=caption, has_spoiler=True)
    except TypeError:
        await app.send_photo(m.chat.id, START_IMAGE, caption=caption)
