import inspect
import re
import os
from pathlib import Path
from telethon import events
CMD_LIST = {}
LOAD_PLUG = {}
from .session import L2, L3, L4, L5, Legend
bot = Legend

BL_CHAT = "-1001500629429"
SUDO_USERS = os.environ.get("SUDO_USERS")
HANDLER = os.environ.get("COMMAND_HAND_LER", ".")
SUDO_HANDLER = os.environ.get("SUDO_HANDLER", ".")
def legend_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    if pattern is not None:
        global legend_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            legend_reg = sudo_reg = re.compile(pattern)
        else:
            legend_ = "\\" + HANDLER
            sudo_ = "\\" + SUDO_HANDLER
            legend_reg = re.compile(legend_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = legend_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (legend_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
                cmd2 = (
                    (sudo_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})


    def decorator(func):
        if not disable_edited:
            bot.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=legend_reg))
        bot.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=legend_reg))
        if allow_sudo:
            bot.add_event_handler(func, events.NewMessage(**args, from_users=list(SUDO_USERS), pattern=sudo_reg))
        if L2:
            L2.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=legend_reg))
        if L3:
            L3.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=legend_reg))
        if L4:
            L4.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=legend_reg))
        if L5:
            L5.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=legend_reg))
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator

def legend_handler(**args):
    def decorator(func):
        async def wrapper(event):
            await func(event)
        bot.add_event_handler(wrapper, events.NewMessage(**args))
        if L2:
            L2.add_event_handler(wrapper, events.NewMessage(**args))
        if L3:
            L3.add_event_handler(wrapper, events.NewMessage(**args))
        if L4:
            L4.add_event_handler(wrapper, events.NewMessage(**args))
        if L5:
            L5.add_event_handler(wrapper, events.NewMessage(**args))
            
        return wrapper
    
    return decorater

def errors_handler(func):
    async def wrapper(errors):
        try:
            await func(errors)
        except BaseException:

            date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            new = {
                'error': str(sys.exc_info()[1]),
                'date': datetime.datetime.now()
            }

            text = "**LEGENDBOT CRASH REPORT**\n\n"

            link = "[here](https://t.me/legend_userbot)"
            text += "If you wanna you can report it"
            text += f"- just forward this message {link}.\n"
            text += "Nothing is logged except the fact of error and date\n"

            ftext = "\nDisclaimer:\nThis file uploaded ONLY here,"
            ftext += "\nwe logged only fact of error and date,"
            ftext += "\nwe respect your privacy,"
            ftext += "\nyou may not report this error if you've"
            ftext += "\nany confidential data here, no one will see your data\n\n"

            ftext += "--------BEGIN LEGENDBOT TRACEBACK LOG--------"
            ftext += "\nDate: " + date
            ftext += "\nGroup / chat ID: " + str(errors.chat_id)
            ftext += "\nSender ID: " + str(errors.sender_id)
            ftext += "\n\nEvent Trigger:\n"
            ftext += str(errors.text)
            ftext += "\n\nTraceback info:\n"
            ftext += str(traceback.format_exc())
            ftext += "\n\nError text:\n"
            ftext += str(sys.exc_info()[1])
            ftext += "\n\n--------END LEGENDBOT TRACEBACK LOG--------"

            command = "git log --pretty=format:\"%an: %s\" -5"

            ftext += "\n\n\nLast 5 commits:\n"

            process = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE)
            stdout, stderr = await process.communicate()
            result = str(stdout.decode().strip()) \
                + str(stderr.decode().strip())

            ftext += result

    return wrapper
