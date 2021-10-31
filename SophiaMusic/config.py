import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Worldwide_friends_chatting_zonee")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/bdaf6ec4f68d49ce3a411.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "NA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Worldwide_friends_chatting_zonee")
PROJECT_NAME = getenv("PROJECT_NAME", "Army")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/itzharshit/army")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
PMMSG = getenv("PMMSG", f"Hi there, This is a music assistant service of @{BOT_USERNAME} created by @army0071.\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you are sending a message here it means admin will see your message and join chat\n    - Don t add this user to secret groups.\n   - Don t Share private info here\n\n")
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/bdaf6ec4f68d49ce3a411.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
