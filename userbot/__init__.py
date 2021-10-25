import os
import sys
import time
from telethon.sessions import StringSession
from telethon import TelegramClient
from userbot.config.Config import Config
from var import Var
from .startup.connect import *
from .startup import *
from .k import *
BOTLOG = True
StartTime = time.time()
LEGENDversion = "𝚅3.𝙾"
botversion = "𝚅3.𝙾"
log = os.environ.get("LOGGER_ID")

#New Tcp
bot = Legend
tbot = LegendBot

#LEGEND = bot
DEVS = [
    "1938996006"
       ]
CMD_LIST = {}
# for later purposes
CMD_HELP = {}
CMD_HELP_BOT = {}
BRAIN_CHECKER = []
INT_PLUG = ""
LOAD_PLUG = {}

# PaperPlaneExtended Support Vars
ENV = os.environ.get("ENV", False)

LEGEND_ID = ["1938996006"]

""" PPE initialization. """

from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
import asyncio

import pylast
from pySmartDL import SmartDL
from requests import get
# Bot Logs setup:
if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=INFO)
    LOGS = getLogger("[LEGEND BOT 3.0]")

try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except:
    HEROKU_APP = None



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

if not dB.get("COMMAND_HAND_LER"):
    dB.set("COMMAND_HAND_LER", ".")

if not dB.get("LOGGER_ID"):
    try:
        dB.set("LOGGER_ID", log)
    except:
        dB.set("LOGGER_ID", "-100")
    
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
