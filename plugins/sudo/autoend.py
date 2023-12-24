from pyrogram import filters

from Bikash import config
from Bikash.Bgt import get_command
from Bikash import app
from Bikash.misc import SUDOERS
from Bikash.utils.database import autoend_off, autoend_on
from Bikash.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**Usage 👇:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "Auto End Stream Enable .\n\nBot Assistant Will Leave Chat Automatically After 3 min Is  Listening With  A Warning message "
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("🥀 𝐀𝐮𝐭𝐨 𝐒𝐭𝐫𝐞𝐚𝐦 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 ✅")
    else:
        await message.reply_text(usage)
