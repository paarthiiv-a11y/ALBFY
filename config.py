import os

# ── telegram credentials ─────────────────────────────────────────────────────
API_ID    = int(os.getenv("API_ID", "11983645"))
API_HASH  = os.getenv("API_HASH", "67645172751678bec31dc03a1548cbe5")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# ── developer info ───────────────────────────────────────────────────────────
DEV_URL = os.getenv("DEV_URL", "https://t.me/DmOwner")

# ── log channel ──────────────────────────────────────────────────────────────
# set to your private channel's numeric id, e.g. -1001234567890
# leave as 0 to disable logging
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))

# ── mongodb ──────────────────────────────────────────────────────────────────
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://videshi:videshi@videshi.wtffv.mongodb.net/?appName=videshi")
DB_NAME   = os.getenv("DB_NAME", "videshi")
