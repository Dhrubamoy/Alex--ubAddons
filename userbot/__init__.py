import os
import sys
import time
from telethon.sessions import StringSession
from telethon import TelegramClient
from userbot.Config import Config
from var import Var
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
BOTLOG = True
StartTime = time.time()
LEGENDversion = "𝚅3.0"
botversion = "𝚅3.0"
from .Config import *
if Config.LEGEND_STRING:
    session = StringSession(str(Config.LEGEND_STRING))
else:
    session = "legendbot"


try:
    Legend = TelegramClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"LEGEND_STRING - {e}")
    sys.exit()


LegendBot = TelegramClient(
    session="Legend-Bot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.BOT_TOKEN)


bot = kbot = Legend
tbot = LegendBot


DEVS = ["2082798662"]
CMD_LIST = {}
# for later purposes
CMD_HELP = {}
CMD_HELP_BOT = {}
BRAIN_CHECKER = []
INT_PLUG = ""
LOAD_PLUG = {}

# PaperPlaneExtended Support Vars
ENV = os.environ.get("ENV", False)

LEGEND_ID = ["2082798662"]

""" PPE initialization. """

from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
import asyncio

import pylast
from pySmartDL import SmartDL
from requests import get
# Bot Logs setup:

# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
SUDO_LIST = {}


from userbot.helpers import *
from userbot.cmdhelp import CmdHelp
