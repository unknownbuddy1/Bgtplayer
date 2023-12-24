from pyrogram import filters
from pyrogram.types import Message

from Bikash.config import BANNED_USERS
from Bikash import app
from Bikash.core.call import Bikashh
from Bikash.utils.database import is_muted, mute_on
from Bikash.utils.decorators import AdminRightsCheck


@app.on_message(
    filters.command(["mute", "cmute"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text("**❌ Error,Wrong Usage Of Command ❗...**")
    if await is_muted(chat_id):
        return await message.reply_text("**🔇 Music Bot is already Muted 🌷 ...**")
    await mute_on(chat_id)
    await Bikashh.mute_stream(chat_id)
    await message.reply_text("**🔇 Muted 🌷 ...**\n\n⎿Requested by > {}")
