from Tnc import *
import asyncio
from pyrogram import filters
from main import app
from utils.database import COL

OWNER_ID = 8487284125

@app.on_message(filters.command("broadcast") & filters.private)
async def broadcast_cmd(_, m):
    if not m.from_user or m.from_user.id != OWNER_ID:
        return await m.reply_text("Only the bot owner can use this command.")
    if len(m.command) < 2:
        return await m.reply_text("Usage: /broadcast Your message here")
    text = m.text.split(" ", 1)[1]
    chats = []
    async for doc in COL.find({}, {"_id":0, "chat_id":1}):
        if "chat_id" in doc:
            chats.append(doc["chat_id"])
    sent = 0
    for c in chats:
        try:
            await app.send_message(c, text)
            sent += 1
        except:
            pass
    await m.reply_text("✅ Broadcast sent to {} chats.".format(sent))
    
@app.on_message(filters.command("broadcast_user") & filters.private)
async def broadcast_user_cmd(_, m):
    if not m.from_user or m.from_user.id != OWNER_ID:
        return await m.reply_text("Only the bot owner can use this command.")
    if len(m.command) < 2:
        return await m.reply_text("Usage: /broadcast_user Your message here")
    text = m.text.split(" ", 1)[1]
    users = []
    async for doc in COL.find({"type":"user"}, {"_id":0, "chat_id":1}):
        if "chat_id" in doc:
            users.append(doc["chat_id"])
    sent = 0
    for u in users:
        try:
            await app.send_message(u, text)
            sent += 1
        except:
            pass
    await m.reply_text("✅ Broadcast sent to {} users.".format(sent))
