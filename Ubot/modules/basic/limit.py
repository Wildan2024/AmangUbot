# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT

import asyncio
from pyrogram import Client, filters, raw
from pyrogram.types import Message
from . import *
from ubotlibs.ubot.helper.basic import edit_or_reply


@Ubot(["limit"], "")
async def spamban(client: Client, m: Message):
    await client.unblock_user("SpamBot")
    response = await client.send(
        raw.functions.messages.StartBot(
            bot=await client.resolve_peer("SpamBot"),
            peer=await client.resolve_peer("SpamBot"),
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    mm = await m.reply_text("`Processing...`")
    await asyncio.sleep(1)
    await mm.delete()
    spambot_msg = response.updates[1].message.id + 1
    status = await client.get_messages(chat_id="SpamBot", message_ids=spambot_msg)
    await m.edit_text(f"~ {status.text}")

add_command_help(
    "limit",
    [
        [f"limit", "Cek limit/batasan akun."],
    ],
)