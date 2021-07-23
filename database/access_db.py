import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from database.database import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)