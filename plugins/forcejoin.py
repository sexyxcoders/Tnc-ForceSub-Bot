from Tnc import *
import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from main import app
from utils.database import set_force_channel, get_force_channel, disable_force, get_warn_mode, set_warn_mode

async def is_admin(chat_id, user_id):
    try:
        admins = [a.user.id for a in await app.get_chat_administrators(chat_id)]
        return user_id in admins
    except:
        return False

@app.on_message(filters.command("fsub") & filters.group)
async def fsub_command(_, m):
    if not m.from_user:
        return
    if not await is_admin(m.chat.id, m.from_user.id):
        return await m.reply_text("Only admins can use this command!")
    if len(m.command) == 1:
        channel = await get_force_channel(m.chat.id)
        if not channel:
            return await m.reply_text("No force join channel set.")
        return await m.reply_text("Current force join: `{}`".format(channel))
    arg = m.command[1]
    if arg.lower() == "off" or arg.lower() == "disable":
        await disable_force(m.chat.id)
        await m.reply_text("{} Force join disabled.".format(EMOJI_SUCCESS))
    else:
        await set_force_channel(m.chat.id, arg.replace("@", ""))
        await m.reply_text("{} Force join set to @{}".format(EMOJI_SUCCESS, arg.replace("@", "")))

@app.on_message(filters.command("fstatus") & filters.group)
async def fstatus_command(_, m):
    channel = await get_force_channel(m.chat.id)
    if not channel:
        await m.reply_text("🚫 Force Join is disabled.")
    else:
        await m.reply_text("✅ Force Join active for @{}".format(channel), disable_web_page_preview=True)
