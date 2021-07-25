from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class mtb(object):
  
  START_TXT = """
  
<b>Hʏ Bʀᴜʜ  {},👋

I'ᴍ ᴀ Tᴇʟᴇɢʀᴀᴍ Uʀʟ Uᴘʟᴏᴀᴅ Bᴏᴛ 🤖

I Cᴀɴ Uᴘʟᴏᴀᴅ Dɪʀᴇᴄᴛ Lɪɴᴋ Tᴏ Tᴇʟᴇɢʀᴀᴍ Wɪᴛʜᴏᴜᴛ Usɪɴɢ Yᴏᴜʀ Dᴀᴛᴀ Fɪʟᴇ Lɪᴍɪᴛ Is 𝟷.𝟿𝟻GB

Use help Button For More Details

🧨Dᴇᴠᴏʟᴏᴘᴇᴅ & Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ :- <a href='https://t.me/Itz_Me_Malayali'>✯°• Kʀɪsᴛʏ Oꜰꜰᴄɪᴀʟ •°✯ 『★Tᴍ★』 #Broken Sed Life 💔</a></b>
  """
  HELP_TXT = """
  
  **Hy Bro {} It's Not Complicated To Use Me. 😌

Cᴜʀʀᴇɴᴛʟʏ I'ᴍ Sᴜᴘᴘᴏʀᴛɪɴɢ MᴇᴅɪᴀFɪʟᴇ Lɪɴᴋs Tᴏᴏ 
Bᴜᴛ ɪᴛ's Nᴏᴛ Pᴇʀᴍᴀɴᴇɴᴛ 😜

➩ Sᴇɴᴅ Mᴇ Tʜᴇ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Tᴏ Sᴀᴠᴇ Iᴛ Pᴇʀᴍᴀɴᴇɴᴛʟʏ.
➩ Nᴏᴡ Sᴇɴᴅ Mᴇ Tʜᴇ Yᴛᴅʟ Oʀ Dɪʀᴇᴄᴛ Lɪɴᴋ.
➩ Sᴇʟᴇᴄᴛ Tʜᴇ Dᴇsɪʀᴇᴅ Oᴘᴛɪᴏɴ.
➩ Tʜᴇɴ Bᴇ Rᴇʟᴀxᴇᴅ Yᴏᴜʀ Fɪʟᴇ Wɪʟʟ Bᴇ Uᴘʟᴏᴀᴅᴇᴅ Sᴏᴏɴ..

😇 Jᴏɪɴ :- <a href='https://t.me/HiroshiBots'>HɪʀᴏsʜɪBᴏᴛs</a> &  <a href='https://t.me/HiroshiBotsSupport'>HɪʀᴏsʜɪBᴏᴛsSᴜᴘᴘᴏʀᴛ</a>
"""
  
  ABOUT_TXT = """
  
<b>🎆My Name : <a href='https://t.me/URLHiroshiBot'>URL Uploader Hiroshi Bot</a></b>\n
<b>👩‍🦽Version : <a href='https://t.me/URLHiroshiBot'>0.9.2 beta</a></b>\n
<b>⛑Source : <a href='https://t.me/WantSourceCode'>Click Here</a></b>\n
<b>⚙️Server : <a href='https://heroku.com'>Heroku</a></b>\n
<b>🛡Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>\n
<b>🪓Language : <a href='https://www.python.org'>Python 3.9.4</a></b>\n
<b>🎉Developer : <a href='https://t.me/Itz_Me_Malayaali'>✯°• Kʀɪsᴛʏ Oꜰꜰᴄɪᴀʟ •°✯</a></b>\n
<b>🚀Channel : <a href='https://t.me/HiroshiBots'>𝗛𝗶𝗿𝗼𝘀𝗵𝗶 𝗕𝗼𝘁𝘀</a></b>\n
"""
  
  START_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("💁🏻 𝑴𝒚 𝑭𝒂𝒕𝒉𝒆𝒓", url="https://t.me/Itz_Me_Malayali"),
      InlineKeyboardButton("⚙️ 𝑯𝒆𝒍𝒑", callback_data="help")
     ],[
      InlineKeyboardButton("𝑨𝒃𝒐𝒖𝒕 📕", callback_data="about"),
      InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆 🔐", callback_data="close")
    ]]
    )
      
  HELP_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("🔙 𝑩𝒂𝒄𝒌", callback_data="home"),
      InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆 🔐", callback_data="close")
    ]]
    )
  
  ABOUT_BUTTONS = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("🔙 𝑩𝒂𝒄𝒌", callback_data="home"),
      InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆 🔐", callback_data="close")
    ]]
    )
