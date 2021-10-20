import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
try:
  from userbot import bot 
except:
  pass
from userbot import *
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
kbot = TelegramClient("legend", API_ID, API_HASH).start(bot_token=token)


if __name__=="__main__":
  bot.start()
  bot.run_until_disconnected()
  kbot.run_until_disconnected()
