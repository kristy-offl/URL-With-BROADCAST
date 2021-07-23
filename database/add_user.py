import os
if bool(os.environ.get("WEBHOOK", False)):
  from config import Config
else:
  from sample_config import Config

from database.access_db import db
from pyrogram import Client
from pyrogram.types import Message


async def AddUserToDatabase(c: Client, m: Message):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await c.send_message(
                int(Config.LOG_CHANNEL),
                f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) started @{(await c.get_me()).username} !!"
            )
