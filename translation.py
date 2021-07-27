from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hello {} , I'am a url to telegram file or media uploader bot with permanent thumbnail support.

Made by @FayasNoushad
"""
    HELP_TEXT = """
<b><u>Link to Media or File</u></b>
➠ Send a link for upload to telegram file or media.

<b><u>Set Thumbnail</u></b>
➠ Send a photo to make it as permanent thumbnail.

<b><u>Deleting Thumbnail</u></b>
➠ Send /delthumb to deleting thumbnail.

<b><u>Show Thumbnail</u></b>
➠ Send /showthumb to view custom thumbnail.

Made by @FayasNoushad
"""
    ABOUT_TEXT = """
- **Bot :** `URL Uploader`
- **Creator :** [Fayas](https://telegram.me/TheFayas)
- **Channel :** [Fayas Noushad](https://telegram.me/FayasNoushad)
- **Credits :** `Everyone in this journey`
- **Source :** [Click here](https://github.com/FayasNoushad/URL-Uploader)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url='https://telegram.me/FayasNoushad'),
        InlineKeyboardButton('Feedback', url='https://telegram.me/TheFayas')
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = """<b>Select the desired format:</b> <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /delthumb to delete the auto-generated thumbnail."""
    UPGRADE_TEXT = "𝙏𝙝𝙖𝙣𝙠𝙨 𝙛𝙤𝙧 𝙨𝙝𝙤𝙬𝙞𝙣𝙜 𝙞𝙣𝙩𝙚𝙧𝙚𝙨𝙩 𝙞𝙣 𝙙𝙤𝙣𝙖𝙩𝙞𝙤𝙣.\n\n𝑪𝒐𝒏𝒕𝒂𝒄𝒕 𝑫𝒆𝒗𝒐𝒍𝒐𝒑𝒆𝒓 𝑩𝒚 𝑪𝒍𝒊𝒄𝒌𝒊𝒏𝒈 𝑩𝒆𝒍𝒐𝒘 𝑩𝒖𝒕𝒕𝒐𝒏😊"
    STATS_TEXT = """
╭─────────[ <a href='https://t.me/HiroshiBots'>𝑩𝒐𝒕 𝑺𝒕𝒂𝒕𝒔</a> ]─────────
│
├⏱️ 𝑼𝒑 𝑻𝒊𝒎𝒆 : 15Hrs : 21Mins : 12Sec
│
├📦 𝑻𝒐𝒕𝒂𝒍 𝑫𝒊𝒔𝒌 𝑺𝒑𝒂𝒄𝒆 : 500.42 GB
│
├📀 𝑼𝒔𝒆𝒅 : 181.71 GB
│
├💿 𝑭𝒓𝒆𝒆 : 293.27 GB
│
╰─────────[ <a href='https://t.me/HiroshiBots'>𝑯𝒊𝒓𝒐𝒔𝒉𝒊 𝑩𝒐𝒕𝒔</a> ]────────
    """
    CHECKING_LINK = "<code>Analysing Your Link</code>⏳"
    STATS_TEXT = """
def stats(update, context):
    currentTime = get_readable_time(time.time() - botStartTime)
    total, used, free = shutil.disk_usage('.')
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
    recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    stats = f'<b>Bot Uptime:</b> {currentTime}\n' \
            f'<b>Total Disk Space:</b> {total}\n' \
            f'<b>Used:</b> {used}  ' \
            f'<b>Free:</b> {free}\n\n' \
            f'📊Data Usage📊\n<b>Upload:</b> {sent}\n' \
            f'<b>Download:</b> {recv}\n\n' \
            f'<b>CPU:</b> {cpuUsage}%\n' \
            f'<b>RAM:</b> {memory}%\n' \
            f'<b>DISK:</b> {disk}%'
    sendMessage(stats, context.bot, update)
"""
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""
    DOWNLOAD_START = "<code>Downloading To My server Please Wait...</code>"    
    UPLOAD_START = "<code>Uploading into Telegram...</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> @FayasNoushad"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me 😌😉....</code>"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
