from pathlib import Path
import glob
from userbot.utils import load_module, start_assistant, load_addons, load_abuse 
async def module():
  import glob
  path = 'userbot/plugins/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))
    
assistant = os.environ.get("ASSISTANT", None)
async def assistants():
    if assistant == "ON":
        path = "userbot/plugins/assistant/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_assistant(shortname.replace(".py", ""))

addon = os.environ.get("EXTRA_PLUGIN", None)             
async def addons():
    if addon == "ON":
        extra_repo = "https://github.com/LEGEND-OS/LegendBot-Addons"
        try:
            os.system(f"git clone {extra_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("🔱🏆Loading Extra Plugin🏆🔱")
        path = "LegendBot-Addons/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"[LEGEND-BOT 2.1] - Addons -  ✅Installed✅ - {shortname}")
                except Exception as e:
                    LOGS.warning(f"[LEGEND-BOT 2.1] - Addons - ⚠️⚡ERROR⚡⚠️ - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Addons Not Loading")
        
abuse = os.environ.get("ABUSE", None) 
async def abuses():
    if abuse == "ON":
        abuse_repo = "https://github.com/LEGEND-OS/ABUSE"
        try:
            os.system(f"git clone {abuse_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("🤬🤪 Loding Abuse 🤪🤬")
        path = "ABUSE/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_abuse(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"[LEGEND-BOT 2.1] - Abuse -  🔥📍Installed✔ - {shortname}")
                except Exception as e:
                    LOGS.warning(f"[LEGEND-BOT 2.1] - Abuse - ⚠️⚡ERROR⚡⚠️ - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Abuse Not Loading")

async def fetch_plugins_from_channel():
    """Fetch Plugins From Channel"""
    try:
        async for message in bot.search_messages(
            Config.PLUGIN_CHANNEL, filter="document", query=".py"
        ):
            hmm = message.document.file_name
            if not os.path.exists(os.path.join("./userbot/plugins/", hmm)):
                await bot.download_media(message, file_name="./userbot/plugins/")
    except BaseException as e:
        LOGS.warning(f"Failed! To Install Plugins From Plugin Channel Due To {e}!")
        return
    LOGS.info("All Plugins From Plugin Channel Loaded!")
