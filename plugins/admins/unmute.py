# Powered By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from pyrogram import filters
from pyrogram.types import Message

from Bikash.config import BANNED_USERS
from Bikash.utils.bgtmusic.bk import command
from Bikash import app
from Bikash.core.call import Bikashh
from Bikash.utils.database import is_muted, mute_off
from Bikash.utils.decorators import AdminRightsCheck


@app.on_message(
    filters.command(["unmute", "cunmute"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text("**❌ Error, Or Wrong Usage Of Command ❗...**")
    if not await is_muted(chat_id):
        return await message.reply_text("**🔊 Already Playing ✨ ...**")
    await mute_off(chat_id)
    await Bikashh.unmute_stream(chat_id)
    await message.reply_text(
        "**🔊 Unmute 🌷 ...**".format(message.from_user.mention)
    )



# PoweredBy @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 
