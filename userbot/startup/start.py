from .. import *
from ..utils import *
from userbot import bot, dB
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
ALIVE_PIC = dB.get("ALIVE_PIC")
LEGEND_PIC = ALIVE_PIC or "https://telegra.ph/file/75e1eda1498620f0030ea.jpg"
from var import Var
from userbot.config.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils import load_module, start_assistant, load_addons
from userbot import LOAD_PLUG, LOGS, LEGENDversion
from pathlib import Path
import asyncio
import telethon.utils
import glob
LOAD_USERBOT = dB.get("LOAD_USERBOT") or False
LOAD_ASSISTANT = dB.get("LOAD_ASSISTANT")

async def module():
  import glob
  path = 'userbot/plugins/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))

async def assistant():
    path = "userbot/plugins/Assistant/*.py"
    files = glob.glob(path)
    for name in files:
      with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))

addon = dB.get("ADDONS") or False                
async def addons():
    if addon == "True":
        extra_repo = "https://github.com/LEGEND-OS/LegendBot-Addons"
        try:
            os.system(f"git clone {extra_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("Loading Addons")
        path = "LegendBot-Addons/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"LEGEND-BOT 3.0 - Addons -  Installed - {shortname}")
                except Exception as e:
                    LOGS.warning(f"LEGEND-BOT 3.0 - Addons - ERROR - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Addons Not Loading")

async def legend_is_on():
    try:
        if dB.get('LOGGER_ID') != 0:
            await bot.send_file(
                dB.get('LOGGER_ID'),
                LEGEND_PIC,
                caption=f"#START \n\nDeployed LEGENDBOT Successfully\n\n**LEGENDBOT- {LEGENDversion}**\n\nType `{ll}op` or `{ll}alive` to check! \n\nJoin [LegendBot Channel](t.me/Its_LegendBot) for Updates & [LegendBot Chat](t.me/Legend_Userbot) for any query regarding LegendBot",
            )
    except Exception as e:
        print(str(e))

# Join LegndBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Its_LegendBot"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@Legend_Userbot"))
    except BaseException:
         pass
