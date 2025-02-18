import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7505862917:AAFXiQ9GGT6gZ8bjhOjjXkVPf0__Zply2xs")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29052852"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0af68ba2f02e73ee4909678f33f8810c")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002282114461"))

#auto delete time 
HK_SECONDS = int(os.environ.get("HK_SECONDS", "900"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5150993718"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://iakshaytayade:iakshaytayade@cluster0.7ujhg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "iakshaytayade")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-100xxxxxxxxx"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4")) 

START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5150993718").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", " {filename}\n\n<b>Movies Channel</b> :- https://t.me/+nDTaoJGRKJcxYmZl")

#CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", " {file_name}](https://t.me/+S33Ihxlur5wwMjRl)\n\n<b>•────•────────•────•\n📌 ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/+nDTaoJGRKJcxYmZl)\n🎬 ᴍᴏᴠɪᴇs ᴄʜᴀɴɴᴇʟ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/KR_Movie2)\n•────•────────•────•\n\n©️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ʜᴀʀɪ ʙᴏᴛᴢ](https://t.me/TG_BOTS_UPDATE /n/n🚫 ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴄʟᴏsᴇ ʙᴜᴛᴛᴏɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ sᴇᴇɴ ᴛʜᴇ ᴍᴏᴠɪᴇ 🚫

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Hey Bro/Sis Don't send me messages directly.... I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(7253187871)

LOG_FILE_NAME = "HK_FS_Bot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
