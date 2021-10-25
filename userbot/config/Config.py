import os
from ..startup.connect import dB
from telethon.tl.types import ChatBannedRights
ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os
    class Config(object):
        LOGGER = True
        # Get this value from my.telegram.org! Please do not steal
        LOCATION = dB.get("LOCATION")
        OPEN_WEATHER_MAP_APPID = dB.get("OPEN_WEATHER_MAP_APPID")
        # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture
        SCREEN_SHOT_LAYER_ACCESS_KEY = dB.get("SCREEN_SHOT_LAYER_ACCESS_KEY")
        # Send .get_id in any group to fill this value.
        SUDO_COMMAND_HAND_LER = dB.get("SUDO_COMMAND_HAND_LER")

        # This is required for the plugins involving the file system.
        TMP_DOWNLOAD_DIRECTORY = dB.get("TMP_DOWNLOAD_DIRECTORY") or "./userbot/DOWNLOADS/"
        # This is required for the speech to text module. Get your USERNAME from https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
        IBM_WATSON_CRED_URL = dB.get("IBM_WATSON_CRED_URL")
        IBM_WATSON_CRED_PASSWORD = dB.get("IBM_WATSON_CRED_PASSWORD")
        # This is required for the hash to torrent file functionality to work.
        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "LEGENDBOT")

        # Send .get_id in any group with all your administration bots (added)
        G_BAN_LOGGER_GROUP = dB.get("LOG_GROUP")
        # TG API limit. An album can have atmost 10 media!
        FBAN_LOGGER_GROUP = dB.get("LOG_GROUP")
        if FBAN_LOGGER_GROUP:
            FBAN_LOGGER_GROUP = int(FBAN_LOGGER_GROUP)

        GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
        TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        # MIRROR ACE API KEY AND TOKEN
        # Telegram BOT Token from @Bot
        #spootifie
        SPOTIFY_USERNAME = dB.get("SPOTIFY_USERNAME")
        SPOTIFY_PASS = dB.get("SPOTIFY_PASS")
        SPOTIFY_BIO_PREFIX = dB.get("SPOTIFY_BIO_PREFIX")
        #log
        DUAL_LOG = os.environ.get("DUAL_LOG", None)
        # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
        # TG API limit. A message can have maximum 4096 characters!
        MAX_MESSAGE_SIZE_LIMIT = 4095
        # set blacklist_chats where you do not want userbot's features
        UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
        # maximum number of messages for antiflood
        MAX_ANTI_FLOOD_MESSAGES = 10
        # warn mode for anti flood
        ANTI_FLOOD_WARN_MODE = ChatBannedRights(
            until_date=None,
            view_messages=None,
            send_messages=True
        )
        # chat ids or usernames, it is recommended to use chat ids,
        # providing usernames means an additional overhead for the user
        CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
        # Get your own API key from https://www.remove.bg/ or
        # feel free to use http://telegram.dog/Remove_BGBot
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        # Set to True if you want to block users that are spamming your PMs.
        SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
        GITHUB_ACCESS_TOKEN = dB.get("GITHUB_ACCESS_TOKEN")
        GIT_REPO_NAME = dB.get("GIT_REPO_NAME")
        NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", True))
        # define "spam" in PMs
        NO_SONGS = bool(os.environ.get("NO_SONGS", False))
        MAX_FLOOD_IN_PM = int(os.environ.get("MAX_FLOOD_IN_PM", 5))
        #pm log
        PM_LOG_GRP_ID = os.environ.get("PM_LOG_GRP_ID", None)
        # set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
        NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", True))
        #heroku 
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
        HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
        # send .get_id in any channel to forward all your NEW PMs to this group
        PRIVATE_GROUP_BOT_API_ID = dB.get("LOG_GROUP")
        if PRIVATE_GROUP_BOT_API_ID:
            PRIVATE_GROUP_BOT_API_ID = int(PRIVATE_GROUP_BOT_API_ID)
        # send .get_id in your private channel to forward all your Private messages

        TAG_LOGGER = dB.get("LOG_GROUP")
        if TAG_LOGGER: TAG_LOGGER = int(TAG_LOGGER)

        #Tag LOGGER

        PM_LOGGR_BOT_API_ID = dB.get("LOG_GROUP")
        if PM_LOGGR_BOT_API_ID: PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
        # For Databases
        # can be None in which case plugins requiring
        # DataBase would not work
        DB_URI = os.environ.get("DATABASE_URL", None)
        # number of rows of buttons to be displayed in .legend command
        BUTTONS_IN_HELP = int(os.environ.get("NO_OF_BUTTONS", 7))
        #open load
        OPEN_LOAD_LOGIN = dB.get("OPEN_LOAD_LOGIN")
        OPEN_LOAD_KEY = dB.get("OPEN_LOAD_KEY")
        # number of colums of buttons to be displayed in .legend command
        NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = int(os.environ.get("NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD", 2))
        # emoji to be displayed  in help .legend
        EMOJI_IN_HELP1 = dB.get("EMOJI_IN_HELP") or "✘"
        EMOJI_IN_HELP2 = dB.get("EMOJI_IN_HELP2") or "✘"
        # specify command handler that should be used for the plugins
        # this should be a valid "regex" pattern
        COMMAND_HAND_LER = dB.get("COMMAND_HAND_LER")
        HANDLER = COMMAND_HAND_LER
        #custom animation to kang plugin
        CUSTOM_STICKER_PACK_NAME = dB.get("CUSTOM_STICKER_PACK_NAME")
        # specify list of users allowed to use bot
        # WARNING: be careful who you grant access to your bot.
        # malicious users could do ".exec rm -rf /*"
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        # VeryStream only supports video formats
        VERY_STREAM_LOGIN = dB.get("VERY_STREAM_LOGIN")
        VERY_STREAM_KEY = dB.get("VERY_STREAM_KEY")
        GROUP_REG_SED_EX_BOT_S = dB.get("GROUP_REG_SED_EX_BOT_S") or "(regex|moku|BananaButler_|rgx|l4mR)bot"
        TEMP_DIR = os.environ.get("TEMP_DIR", None)
        CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
        watermark_path = os.environ.get("watermark_path", None)
        #Google Chrome Stuff
        CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver")
        GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
        # Google Drive ()
        G_DRIVE_CLIENT_ID = dB.get("G_DRIVE_CLIENT_ID")
        G_DRIVE_CLIENT_SECRET = dB.get("G_DRIVE_CLIENT_SECRET")
        GDRIVE_FOLDER_ID = dB.get("GDRIVE_FOLDER_ID")
        AUTH_TOKEN_DATA = dB.get("AUTH_TOKEN_DATA")
        if AUTH_TOKEN_DATA != None:
            os.makedirs(TMP_DOWNLOAD_DIRECTORY)
            t_file = open(TMP_DOWNLOAD_DIRECTORY+"auth_token.txt","w")
            t_file.write(AUTH_TOKEN_DATA)
            t_file.close()

        YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        #alive
        ALIVE_PIC = dB.get("ALIVE_PIC")
        PM_PIC = dB.get("PM_PIC")
        AWAKE_PIC = dB.get("AWAKE_PIC")
        HELP_PIC = dB.get("OP_PIC")
        ALIVE_MSG = dB.get("ALIVE_MSG")
        PM_MSG = dB.get("PM_MSG")
        INSTANT_BLOCK = dB.get("INSTANT_BLOCK") or "ENABLE"
        YOUR_GROUP = "@Legend_Userbot"
        YOUR_CHANNEL = "@Its_LegendBot"
        BOT_PIC = dB.get("ALIVE_PIC")
        #auto bio
        BIO_MSG = dB.get("ALIVE_MSG")
        PLUGIN_CHANNEL = dB.get("PLUGIN_CHANNEL")
        UPSTREAM_REPO = os.environ.get(
            "UPSTREAM_REPO", "https://github.com/LEGEND-OS/LEGENDBOT"
        )
        LEGEND_STRING = os.environ.get("LEGEND_STRING")
        BOT_MODE = dB.get("BOT_MODE") or "ON"
        ABUSE = dB.get("ABUSE")
        BOTLOG_CHATID = dB.get("LOG_GROUP")
        ALIVE_NAME = dB.get("ALIVE_NAME")
        BOY_OR_GIRL = os.environ.get("BOY_OR_GIRL")
        BOT_TRIGGER = os.environ.get("BOT_TRIGGER") or "^/"
        BOTMODE_LOG = int(os.environ.get("BOTMODE_LOG", False))
        BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
        BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
        FORCE_SUB = dB.get("FORCE_SUB")
        FORCE_CHANNEL_UN = dB.get("FORCE_CHANNEL_UN")
        LOGGER_ID = dB.get("LOG_GROUP")
        if LOGGER_ID:
            LOGGER_ID = int(LOGGER_ID)
        FORCE_CHANNEL_ID = int(os.environ.get("FORCE_CHANNEL_ID", False))
        EXTRA_LEGENDBOT = os.environ.get("EXTRA_LEGENDBOT", -1001221881562)
        PM_DATA = os.environ.get("PM_DATA", "ENABLE")

else:
    class Config(object):
        DB_URI = None
