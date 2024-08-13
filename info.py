import os
import re
from os import environ, getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get("API_ID", "23093909"))
API_HASH = environ.get("API_HASH", "78b1573e7f678234c4f83d5ae5da4b26")
BOT_TOKEN = environ.get("BOT_TOKEN", "6163005421:AAGyIa3RVaIKr0TS-tHX2uTWsVIU2EHjNmI")
BOT_ID = int(environ.get("BOT_ID", "6163005421"))
BOT_CMD = ['/', '.', '?', '-', '+', '!']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled((environ.get('USE_CAPTION_FILTER', 'True')), True)

PICS = (environ.get('PICS', 'https://telegra.ph/file/d6b4ef8dca4b93bc21cb9.jpg https://telegra.ph/file/991d7fced2ca3c6b57ef6.jpg https://telegra.ph/file/c02d3f4f41b4613e08bdc.jpg https://telegra.ph/file/a588dd1a1c8851ed95961.jpg https://telegra.ph/file/29ddc89f6e7640020599a.jpg https://telegra.ph/file/3f7028199d9852f434e60.jpg https://telegra.ph/file/ea17395db32a8ebd060e9.jpg https://telegra.ph/file/9d67204266920e978e602.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/703c3040bcd811991aae5.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/f7f2a532fe4b990044507.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/5e2d4418525832bc9a1b9.jpg")

NETWORK_CHANNEL = environ.get('NETWORK_CHANNEL', 'Cinepaiyan_Movies') # Movie Channel
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/+i8_fLzb5cjowYzE9') # Movie Channel
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+5x_HhwVsIgs3ZTk1') # Movie Request Group
UPDATES_CHANNEL = environ.get('UPDATES_CHANNEL', 'https://t.me/ThiruEmpire') # Bots Channel or any update channel
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/ThiruSupport') # Bots support group or any chat group

# Admins, Channels & Users
OWNER = environ.get('OWNER', '1132179847').split()
OWNER_USERNAME = environ.get('OWNER_USERNAME', 'Team_Tom24') # Without https://t.me & @
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1351421131 1989750989').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002064486321 -1001932461399').split()]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001642817829))
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1002140715188')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = is_enabled((environ.get("NO_RESULTS_MSG", 'False')), False)

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://leechone:leechone@leechone.rvdh2qk.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cinepaiyan_Movies_Bot")
DB_NAME_TWO = environ.get('DB_NAME_TWO', "Cinepaiyan_Movies_Bot_walt")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Shortner details
IS_VERIFY = is_enabled((environ.get('IS_VERIFY', 'False')), False)
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', "https://t.me/c/1845700490/3")
VERIFY2_URL = environ.get('VERIFY2_URL', "mdisklink.link")
VERIFY2_API = environ.get('VERIFY2_API', "4fa150d44b4bf6579c24b33bbbb786dbfb4fc673")
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'clicksfly.com')
SHORTLINK_API = environ.get('SHORTLINK_API', 'c2150e28189cefefd05f8a9c5c5770cc462033e3')
IS_SHORTLINK = is_enabled((environ.get('IS_SHORTLINK', 'False')), False)

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# More Features
HRK_API = environ.get("HRK_API", "71838cdc-1efd-48a4-967f-18d3eb8ef5f3")
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

#Openai
AI = is_enabled((environ.get("AI","True")), True)
OPENAI_API = environ.get("OPENAI_API","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")
AI_LOGS = int(environ.get("AI_LOGS","-1001642817829"))


LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
