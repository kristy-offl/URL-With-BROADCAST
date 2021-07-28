import time
import shutil, psutil
import signal
import os

from pyrogram import Client, filters

bot_start_time = time.time()

@Client.on_message(filters.command(["stats"]) & filters.private)
async def stats_text(bot, update):
    await bot.send_message(
         chat_id=update.chat.id,
         await message.reply_text("uptime = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - bot_start_time)),
         parse_mode="html",
         reply_to_message_id=update.message_id,
         disable_web_page_preview=True
        )

