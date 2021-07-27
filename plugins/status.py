import shutil, psutil
import signal
import os

from bot import status, dispatcher, updater, botStartTime
from status import status get_readable_file_size, get_readable_time

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
