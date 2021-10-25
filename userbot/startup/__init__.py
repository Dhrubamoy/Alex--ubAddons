from .decs import legend_cmd
from .session import Legend, L2, L3, L4, L5, LegendBot
import telethon.utils
from userbot import *


async def clients_list(Config, Legend, L2, L3, L4, L5):
    user_ids = list(Config.SUDO_USERS) or []
    main_id = await Legend.get_me()
    user_ids.append(main_id.id)

    try:
        if L2 is not None:
            id2 = await L2.get_me()
            user_ids.append(id2.id)
    except:
        pass

    try:
        if L3 is not None:
            id3 = await L3.get_me()
            user_ids.append(id3.id)
    except:
        pass

    try:
        if L4 is not None:
            id4 = await L4.get_me()
            user_ids.append(id4.id)
    except:
        pass

    try:
        if L5 is not None:
            id5 = await L5.get_me()
            user_ids.append(id5.id)
    except:
        pass

    return user_ids


async def client_id(event):
    client = await event.client.get_me()
    uid = telethon.utils.get_peer_id(client)
    Its_LegendBoy = uid
    LEGEND_USER = client.first_name
    legend_mention = f"[{LEGEND_USER}](tg://user?id={Its_LegendBoy})"
    client = await event.client.get_me()
    uid = telethon.utils.get_peer_id(client)
    ForGo10God = uid
    HELL_USER = client.first_name
    hell_mention = f"[{HELL_USER}](tg://user?id={ForGo10God})"
    return Its_LegendBoy, LEGEND_USER, legend_mention, ForGo10God, HELL_USER, hell_mention # Added Support of Hellbot Support on public request
