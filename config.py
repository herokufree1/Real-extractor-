"""
from os import getenv


API_ID = int(getenv("API_ID", "16253557"))
API_HASH = getenv("API_HASH", "81171c25e4cb9062cb10da8b7730432a")
BOT_TOKEN = getenv("BOT_TOKEN", "7923836196:AAFMTv7Uckt6RFvla8PrzHSK9s02q-8DfRg")
OWNER_ID = int(getenv("OWNER_ID", "1996039956"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1996039956").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002281623908"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002363250260"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "23116888"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "f50411c978f8b138dfcb5a729c18a599")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7675179017:AAEdJy22HhzQms-MhT4IBN-xrFOKGzZ4bhM")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("extractor0121Bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "2073438175"))
# ------------------X------------------------------

THUMB_URL = os.environ.get("THUMB_URL", "https://files.catbox.moe/ao5o4z.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7962530240").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002969140468"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://mongodburl9721:rfNOuo4c1OSTZ7cs@cluster0.edezeww.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# -----------------------------------------------
FORCE_SUB = int(os.environ.get("FORCE_SUB", "-1002975852492"))
TXT_LOG = int(getenv("TXT_LOG", "-1002975852492"))
