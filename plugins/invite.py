from Tnc import *
import asyncio
from pyrogram import filters
from main import app
from utils.database import set_invite_target, get_invite_target, add_invite, get_user_invites

async def is_admin(chat_id, user_id):
    try:
        admins = [a.user.id for a in await app.get_chat_administrators(chat_id)]
        return user_id in admins
    except Exception:
        return False

@app.on_message(filters.command("addsub") & filters.group)
async def addsub_cmd(_, m):
    if not await is_admin(m.chat.id, m.from_user.id):
        return await m.reply_text("Only admins can use this command!")
    if len(m.command) < 2:
        return await m.reply_text("Usage: /addsub <number> or /addsub off")
    arg = m.command[1].lower()
    if arg in ["off", "disable"]:
        await set_invite_target(m.chat.id, 0)
        return await m.reply_text("{} Invite target disabled.".format(EMOJI_SUCCESS))
    try:
        target = int(arg)
        if target <= 0:
            raise ValueError
    except ValueError:
        return await m.reply_text("Please provide a valid positive number.")
    await set_invite_target(m.chat.id, target)
    await m.reply_text("{} Invite target set to {}".format(EMOJI_SUCCESS, target))

@app.on_message(filters.new_chat_members)
async def count_invites(_, m):
    inviter = m.from_user or None
    if not inviter:
        return
    chat_id = m.chat.id
    new_count = len(m.new_chat_members or [])
    await add_invite(chat_id, inviter.id, new_count)
    total = await get_user_invites(chat_id, inviter.id)
    target = await get_invite_target(chat_id)
    if target and total < target:
        await m.reply_text("🎉 {} invited {} member(s). Progress: {}/{}".format(inviter.mention, new_count, total, target))
    elif target and total >= target:
        await m.reply_text("✅ {} has met the invite goal ({}/{})!".format(inviter.mention, total, target))
