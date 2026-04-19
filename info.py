from os import environ
from Script import script

# ================== HELPER FUNCTIONS ==================

def get_int(value, default=0):
    try:
        return int(value)
    except:
        return default

def get_bool(value, default=False):
    return str(value).lower() in ("true", "1", "yes")

def get_list(value):
    return [int(x) for x in str(value).split() if x.lstrip('-').isdigit()]

# 🚀 __Bot Configuration__
SESSION = environ.get('SESSION', 'filetolinkbot')

API_ID = get_int(environ.get('API_ID', '34724970'))
API_HASH = environ.get('API_HASH', 'f240eae7c60e8e30c17203ab0e052f7e')
BOT_TOKEN = environ.get('BOT_TOKEN', '8266205685:AAGbjQwlglgz8TVDs-R1O51xRT3rEyzOEGg')

# 👑 __Owner & Admins__
ADMINS = get_list(environ.get('ADMINS', '7892805795'))
AUTH_CHANNEL = get_list(environ.get("AUTH_CHANNEL", "-1003475522251"))

OWNER_USERNAME = environ.get("OWNER_USERNAME", 'anujedits76')
BOT_USERNAME = environ.get("BOT_USERNAME", 'file_to_link_ak_bot')

# 🔗 __Channel & Support Links__
CHANNEL = environ.get('CHANNEL', 'https://t.me/anujeditbyak')
SUPPORT = environ.get('SUPPORT', 'https://t.me/anujeditbyak')
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', 'https://t.me/anujeditbyak')
HOW_TO_OPEN = environ.get('HOW_TO_OPEN', 'https://t.me/anujeditbyak')

# 📢 __Log Channels__
BIN_CHANNEL = get_int(environ.get("BIN_CHANNEL", '-1003475522251'))
LOG_CHANNEL = get_int(environ.get("LOG_CHANNEL", '-1003475522251'))
PREMIUM_LOGS = get_int(environ.get("PREMIUM_LOGS", '-1003475522251'))
VERIFIED_LOG = get_int(environ.get('VERIFIED_LOG', '-1003475522251'))
SUPPORT_GROUP = get_int(environ.get("SUPPORT_GROUP", "-1003475522251"))

# ✅ __Feature Toggles__
VERIFY = False
FSUB = get_bool(environ.get("FSUB", True))
ENABLE_LIMIT = get_bool(environ.get("ENABLE_LIMIT", True))
BATCH_VERIFY = False
IS_SHORTLINK = False
MAINTENANCE_MODE = get_bool(environ.get("MAINTENANCE_MODE", False))
PROTECT_CONTENT = get_bool(environ.get('PROTECT_CONTENT', False))
PUBLIC_FILE_STORE = get_bool(environ.get('PUBLIC_FILE_STORE', True))
BATCH_PROTECT_CONTENT = get_bool(environ.get('BATCH_PROTECT_CONTENT', False))

# 🔗 __Shortlink Configuration__
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shrink.pe')
SHORTLINK_API = environ.get('SHORTLINK_API', '372b23dabae021f93ca15408fc7a674ec4ec2ce3')

# 💾 __Database Configuration__
DB_URL = environ.get('DATABASE_URI', "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
DB_NAME = environ.get('DATABASE_NAME', "Anujedit")

# 📸 __Media & Images__
QR_CODE = environ.get('QR_CODE', 'https://ibb.co/mVkSySr7')
VERIFY_IMG = environ.get("VERIFY_IMG", "https://ibb.co/mVkSySr7")
AUTH_PICS = environ.get('AUTH_PICS', 'https://ibb.co/mVkSySr7')
PICS = environ.get('PICS', 'https://o.uguu.se/SOCdjMHV.jpg')
FILE_PIC = environ.get('FILE_PIC', 'https://files.catbox.moe/b6vtfh.jpg')

# 📝 __Captions__
FILE_CAPTION = environ.get('FILE_CAPTION', script.CAPTION)
BATCH_FILE_CAPTION = environ.get('BATCH_FILE_CAPTION', script.CAPTION)
CHANNEL_FILE_CAPTION = environ.get('CHANNEL_FILE_CAPTION', script.CAPTION)

# ⏱️ __Time & Limits__
PING_INTERVAL = get_int(environ.get("PING_INTERVAL", 1200))
SLEEP_THRESHOLD = get_int(environ.get('SLEEP_THRESHOLD', 60))
RATE_LIMIT_TIMEOUT = get_int(environ.get("RATE_LIMIT_TIMEOUT", 600))
MAX_FILES = get_int(environ.get("MAX_FILES", 50))
VERIFY_EXPIRE = get_int(environ.get('VERIFY_EXPIRE', 60))
ON_HEROKU = get_bool(environ.get('ON_HEROKU', False))
# ⚙️ __Worker & App Config__
WORKERS = get_int(environ.get('WORKERS', 10))
MULTI_CLIENT = False
NAME = environ.get('name', 'Anujedits76')
ON_HEROKU = get_bool(environ.get('ON_HEROKU', False))
# 🌐 __Web Server__
PORT = get_int(environ.get('PORT', 5000))
NO_PORT = get_bool(environ.get("NO_PORT", "true"))
HAS_SSL = get_bool(environ.get("HAS_SSL", "true"))

# URL Generation
import os as _os
_default_domain = _os.environ.get("REPLIT_DEV_DOMAIN", "file-to-link-bot-jcrf.onrender.com")
BIND_ADDRESS = environ.get("WEB_SERVER_BIND_ADDRESS", _default_domain)
FQDN = environ.get("FQDN", BIND_ADDRESS)

if not str(FQDN).startswith("http"):
    PROTOCOL = "https" if HAS_SSL else "http"
    PORT_SEGMENT = "" if NO_PORT else f":{PORT}"
    FQDN = str(FQDN).rstrip('/')
    URL = f"{PROTOCOL}://{FQDN}{PORT_SEGMENT}/"
else:
    URL = FQDN
