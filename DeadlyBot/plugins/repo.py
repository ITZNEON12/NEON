import random
import re
import time

import requests
from cowpy import cow
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from . import *


@bot.on(admin_cmd(pattern=f"repo", outgoing=True))
@bot.on(sudo_cmd(pattern=f"repo", allow_sudo=True))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(e, "[π²π»πΈπ²πΊ π·π΄ππ΄](https://github.com/DEADLY-FIGHTERS/DeadlY-DANAV-BOT) ππΎ πΎπΏπ΄π½ ππ·πΈπ \nπ₯**π»πΈπ π°π΅!!**π₯ π³π΄π°π³π»π π³π°π½π°π π±πΎπ.\n\n[π π³π΄π°π³π»π π΅πΈπΆπ·ππ΄ππ π](t.ME/DEADLY_FIGHTERS)")

