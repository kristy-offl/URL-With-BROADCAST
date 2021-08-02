from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class mtb(object):
  
  START_TXT = """
  
<b>Hʏ Bʀᴜʜ  {},👋

I'ᴍ ᴀ Tᴇʟᴇɢʀᴀᴍ Uʀʟ Uᴘʟᴏᴀᴅ Bᴏᴛ 🤖

I Cᴀɴ Uᴘʟᴏᴀᴅ Dɪʀᴇᴄᴛ Lɪɴᴋ Tᴏ Tᴇʟᴇɢʀᴀᴍ Wɪᴛʜᴏᴜᴛ Usɪɴɢ Yᴏᴜʀ Dᴀᴛᴀ Fɪʟᴇ Lɪᴍɪᴛ Is 𝟷.𝟿𝟻GB

Nᴏᴛᴇ :- Yᴏᴜ Mᴜsᴛ Sᴇɴᴅ ᴀ Tʜᴜᴍʙɴᴀɪʟ Tᴏ Mᴀᴋᴇ Iᴛ Pᴇʀᴍᴀɴᴇɴᴛ​ & Usᴇ ʜᴇʟᴘ Bᴜᴛᴛᴏɴ Fᴏʀ Mᴏʀᴇ Dᴇᴛᴀɪʟ


🧨Dᴇᴠᴏʟᴏᴘᴇᴅ & Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ :- <a href='https://t.me/Itz_Me_Malayali'>✯°• Kʀɪsᴛʏ Oꜰꜰᴄɪᴀʟ •°✯ 『★Tᴍ★』 #Broken Sed Life 💔</a></b>
  """
  HELP_TXT = """
  
<b>Hʏ Bʀᴏ {} Iᴛ's Nᴏᴛ Cᴏᴍᴘʟɪᴄᴀᴛᴇᴅ Tᴏ Usᴇ Mᴇ. 😌

➩ Sᴇɴᴅ Mᴇ Tʜᴇ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Tᴏ Sᴀᴠᴇ Iᴛ Pᴇʀᴍᴀɴᴇɴᴛʟʏ.
➩ Nᴏᴡ Sᴇɴᴅ Mᴇ Tʜᴇ Yᴛᴅʟ Oʀ Dɪʀᴇᴄᴛ Lɪɴᴋ.
➩ Sᴇʟᴇᴄᴛ Tʜᴇ Dᴇsɪʀᴇᴅ Oᴘᴛɪᴏɴ.
➩ Tʜᴇɴ Bᴇ Rᴇʟᴀxᴇᴅ Yᴏᴜʀ Fɪʟᴇ Wɪʟʟ Bᴇ Uᴘʟᴏᴀᴅᴇᴅ Sᴏᴏɴ..

😇 Jᴏɪɴ :- <a href='https://t.me/HiroshiBots'>HɪʀᴏsʜɪBᴏᴛs</a> &  <a href='https://t.me/HiroshiBotsSupport'>HɪʀᴏsʜɪBᴏᴛsSᴜᴘᴘᴏʀᴛ</a></b>
"""
  
  ABOUT_TXT = """
**🤖 Sᴏᴍᴇᴛʜɪɴɢ Aʙᴏᴜᴛ Mᴇ

• Mʏ Nᴀᴍᴇ : Uʀʟ Uᴘʟᴏᴀᴅᴇʀ HB
• Vᴇʀsɪᴏɴ : 𝟶.𝟿.𝟸 (Bᴇᴛᴀ) 
• Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ : Hɪʀᴏsʜɪ Bᴏᴛs 
• Mʏ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ : Hɪʀᴏsʜɪ Bᴏᴛs Sᴜᴘᴘᴏʀᴛ
• Dᴇᴠᴇʟᴏᴘᴇʀ : ✯°• Kʀɪsᴛʏ Oꜰꜰᴄɪᴀʟ •°✯**
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
