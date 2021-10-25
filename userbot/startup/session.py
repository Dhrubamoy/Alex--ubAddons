from telethon import TelegramClient
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
import sys
from ..config.legendconfig import Config
import os
LEGEND_STRING = os.environ.get("LEGEND_STRING", None)
SESSION_1 = os.environ.get("SESSION_1", None)
SESSION_2 = os.environ.get("SESSION_2", None)
SESSION_3 = os.environ.get("SESSION_3", None)
SESSION_4 = os.environ.get("SESSION_4", None)
SESSION_5 = os.environ.get("SESSION_5", None)

APP_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("API_HASH")

if LEGEND_STRING:
    session = StringSession(str(LEGEND_STRING))
else:
    session = "Legend"
                            
                            
try:
    Legend = TelegramClient(
        session=session,
        api_id=APP_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"LEGEND_STRING - {e}")
    sys.exit()


if SESSION_2:
    session2 = StringSession(str(SESSION_2))
    L2 = TelegramClient(
        session=session2,
        api_id=APP_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    L2 = None


if SESSION_3:
    session3 = StringSession(str(SESSION_3))
    L3 = TelegramClient(
        session=session3,
        api_id=APP_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    L3 = None


if SESSION_4:
    session4 = StringSession(str(SESSION_4))
    L4 = TelegramClient(
        session=session4,
        api_id=APP_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    L4 = None


if SESSION_5:
    session5 = StringSession(str(SESSION_5))
    L5 = TelegramClient(
        session=session5,
        api_id=APP_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    L5 = None
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
LegendBot = TelegramClient(
    session="Legend-Bot",
    api_id=APP_ID,
    api_hash=API_HASH,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=BOT_TOKEN)
