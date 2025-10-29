from Tnc import *
import asyncio
from pyrogram import filters
from main import app
from utils.database import set_force_channel, get_force_channel, disable_force, set_warn_mode, get_warn_mode, register_chat

async def is_admin(chat_id, user_id):
    try:
        admins = [a.user.id for a in await app.get_chat_administrators(chat_id)]
        return user_id in admins
    except Exception:
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
    if arg.lower() in ["off", "disable"]:
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

@app.on_message(filters.command("fwarn") & filters.group)
async def fwarn_command(_, m):
    if not await is_admin(m.chat.id, m.from_user.id):
        return await m.reply_text("Only admins can use this command!")
    if len(m.command) < 2:
        return await m.reply_text("Usage: /fwarn on|off")
    arg = m.command[1].lower()
    if arg == "on":
        await set_warn_mode(m.chat.id, True)
        await m.reply_text("✅ Warnings enabled.")
    elif arg == "off":
        await set_warn_mode(m.chat.id, False)
        await m.reply_text("🔇 Warnings disabled (silent delete).")

@app.on_message(filters.command("ping"))
async def ping_cmd(_, m):
    import time
    start = time.time()
    msg = await m.reply_text("🏓 Pinging...")
    end = time.time()
    await msg.edit_text("🏓 Pong! {} ms".format(int((end-start)*1000)))

@app.on_message(filters.command("stats"))
async def stats_cmd(_, m):
    from utils.database import COL
    total = await COL.count_documents({})
    await m.reply_text("📊 Known chat records: {}".format(total))

@app.on_message(filters.group | filters.private)
async def register_on_message(_, m):
    try:
        if m.chat.type == "private":
            await register_chat(m.chat.id, "user")
        else:
            await register_chat(m.chat.id, "group")
    except:
        pass
