from Tnc import *
from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO = AsyncIOMotorClient(os.getenv("MONGO_URL"))
DB = MONGO.get_database("TncForceJoinBot_v4")
COL = DB.get_collection("forcejoin_config")

async def set_force_channel(chat_id, channel):
    await COL.update_one({"chat_id": chat_id}, {"$set": {"main": channel}}, upsert=True)

async def get_force_channel(chat_id):
    data = await COL.find_one({"chat_id": chat_id})
    return data.get("main") if data else None

async def disable_force(chat_id):
    await COL.update_one({"chat_id": chat_id}, {"$unset": {"main": ""}})

async def set_warn_mode(chat_id, mode: bool):
    await COL.update_one({"chat_id": chat_id}, {"$set": {"warn": mode}}, upsert=True)

async def get_warn_mode(chat_id):
    data = await COL.find_one({"chat_id": chat_id})
    return data.get("warn", True) if data else True

async def register_chat(chat_id, type="group"):
    await COL.update_one({"chat_id": chat_id}, {"$set": {"type": type}}, upsert=True)

# Invite system helpers (kept simple)
async def set_invite_target(chat_id, target: int):
    await COL.update_one({"chat_id": chat_id}, {"$set": {"invite_target": target}}, upsert=True)

async def get_invite_target(chat_id):
    data = await COL.find_one({"chat_id": chat_id})
    return data.get("invite_target", 0) if data else 0

async def add_invite(chat_id, user_id, count=1):
    await COL.update_one({"chat_id": chat_id}, {"$inc": {f"invites.{user_id}": count}}, upsert=True)

async def get_user_invites(chat_id, user_id):
    data = await COL.find_one({"chat_id": chat_id})
    invites = data.get("invites", {}) if data else {}
    return invites.get(str(user_id), invites.get(user_id, 0))

async def get_subchannels(chat_id):
    data = await COL.find_one({"chat_id": chat_id})
    return data.get("subs", []) if data else []

# export COL for broadcast usage
COL = COL
