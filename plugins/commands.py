import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from translation import Translation
from database.add_user import AddUserToDatabase
from database.access_db import db
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await AddUserToDatabase(bot, update)
    await update.reply_text(
        text=mtb.START_TXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=mtb.START_BUTTONS
    )

@Client.on_message(filters.command(["help"])) & filters.private)
async def help_txt(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=mtb.HELP_TXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                 [
                     InlineKeyboardButton('⚙️ 𝑼𝒑𝒅𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍', url='https://t.me/HiroshiBots')
                ],
                [
                    InlineKeyboardButton('📍 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑮𝒓𝒐𝒖𝒑 ', url='https://t.me/HiroshiBotsSupport'), # Bloody Thief, Don't Become a Developer by Stealing other's Codes & Hard Works!
                    InlineKeyboardButton('🙋🏻 𝑫𝒆𝒗𝒐𝒍𝒐𝒑𝒆𝒓 ', url='https://t.me/Abt_Meh') # Must Give us Credits!
                ]
            ]
        ),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
    
@Client.on_message(filters.command(["stats"]))
async def stats_text(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.STATS_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                 [
                     InlineKeyboardButton('⚙️ 𝑼𝒑𝒅𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍', url='https://t.me/HiroshiBots')
                 ]
             ]
         ),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["upgrade"]))
async def upgrade(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                 [
                     InlineKeyboardButton('𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐃𝐞𝐯𝐨𝐥𝐨𝐩𝐞𝐫', url='https://t.me/Itz_Me_Malayali')
                 ]
             ]
         ),
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["about"]))
async def about_text(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                 [
                     InlineKeyboardButton('⚙️ 𝑼𝒑𝒅𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍', url='https://t.me/HiroshiBots')
                ],
                [
                    InlineKeyboardButton('📍 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑮𝒓𝒐𝒖𝒑 ', url='https://t.me/HiroshiBotsSupport'), # Bloody Thief, Don't Become a Developer by Stealing other's Codes & Hard Works!
                    InlineKeyboardButton('🙋🏻 𝑫𝒆𝒗𝒐𝒍𝒐𝒑𝒆𝒓 ', url='https://t.me/Abt_Meh') # Must Give us Credits!
                ]
            ]
        ),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )    
