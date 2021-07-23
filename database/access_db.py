import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from database.mongodb import database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)
