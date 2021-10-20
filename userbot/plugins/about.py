from . import *
import asyncio
import random
from telethon import events
from LEGENDBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"
from userbot.Config import Config
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG
# Thanks to LEGEND BRO.. 
# animation Idea by @The_LegendBoy (op coder)
# Kang with credits else gay...
# alive.py for

edit_time = 10
""" =======================CONSTANTS====================== """
file1="https://telegra.ph/file/639880e214bdcd4a71b7a.jpg"
file2="https://telegra.ph/file/9fb5502699714b8eabca3.jpg"
file3="https://telegra.ph/file/b434509bdfce4ab680fb6.jpg"
file4="https://telegra.ph/file/c113d2da817de44d958a6.jpg"
file5="https://te.legra.ph/file/4e98696debcf92c0f8eb6.jpg"
""" =======================CONSTANTS====================== """
pm_caption = f"** {CUSTOM_ALIVE_TEXT}**\n"
pm_caption += f"**╭────────────**\n"
pm_caption += f"┣»»»『{legend_mention}』«««\n"
pm_caption += f"┣Lêɠêɳ̃dẞø† ~ V•2.1\n"
pm_caption += f"┣Lêɠêɳ̃d  ~ [Owner](https://t.me/The_LegendBoy)\n"
pm_caption += f"┣Support ~ [G𝖗ουρ](https://t.me/Legend_Userbot)\n"
pm_caption += f"┣Řepô    ~ [Rєρο](https://github.com/LEGEND-OS/LEGENDBOT)\n"
pm_caption += f"**╰────────────**\n"
@borg.on(admin_cmd(pattern=r"about"))
@borg.on(sudo_cmd(pattern="about$", allow_sudo=True))
async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file4)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file2)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file1)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file2)
    
    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file3)
    
    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(yes.chat_id, ok10, file=file4)
    
    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(yes.chat_id, ok11, file=file5)
    
    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(yes.chat_id, ok12, file=file1)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("about").add_command(
    "about", None , "BEST alive command"
).add_type(
    "Official"
).add()
