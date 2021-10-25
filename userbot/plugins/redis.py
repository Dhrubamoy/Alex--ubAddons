import re

from . import *
Redis = dB.get

@bot.on(admin_cmd(pattern="setredis")
async def _(event):
    ok = await eor(event, "`...`")
    delim = " " if re.search("[|]", event.pattern_match.group(1)) is None else " | "
    data = event.pattern_match.group(1).split(delim)
    dB.set(data[0], data[1])
    redisdata = Redis(data[0])
    await event.edit(
        "Redis Key Value Pair Updated\nKey : `{}`\nValue : `{}`".format(
            data[0], redisdata
        )
    )

hndlr = dB.get("COMMAND_HAND_LER")
@bot.on(admin_cmd(
    pattern="getredis ?(.*)",
)
async def _(event):
    ok = await eor(event, "`Fetching data from Redis`")
    val = event.pattern_match.group(1)
    if val == "":
        return await event.edit(f"Please use `{hndlr}getkeys <keyname>`")
    else:
        value = Redis(val)
        await event.edit("Key: `{}`\nValue: `{}`".format(val, value))


@bot.on(admin_cmd(
    pattern="delredis ?(.*)"
)
async def _(event):
    ok = await eor(event, "`Deleting data from Redis ...`")
    key = event.pattern_match.group(1)
    dB.delete(key)
    await event.edit(f"`Successfully deleted key {key}`")


@bot.on(admin_cmd(
    pattern="renredis ?(.*)",
)
async def _(event):
    ok = await eor(event, "`Finding`")
    delim = " " if re.search("[|]", event.pattern_match.group(1)) is None else " | "
    data = event.pattern_match.group(1).split(delim)
    if Redis(data[0]):
        dB.rename(data[0], data[1])
        await event.edit(
            "Redis Key Rename Successful\nOld Key : `{}`\nNew Key : `{}`".format(
                data[0], data[1]
            )
        )
    else:
        await event.edit("Key not found")

@bot.on(admin_cmd(
    pattern="getkeys$",
)
async def _(event):
    ok = await eor(event, "`Fetching Keys ...`")
    keys = dB.keys()
    msg = ""
    for x in keys:
        msg += "• `{}`".format(x) + "\n"
    await event.edit("**List of Redis Keys :**\n{}".format(msg))

CmdHelp("redis").add_command(
  "setredis", None, "Save The Values On Redis"
).add_command(
  "getkeys", None, "Sends the keys of your redis"
).add_command(
  "renredis", None, "Renames the redis key"
).add_command(
  "delredis", None, "Deletes the redis key"
).add_warning(
  "Official"
).add()
