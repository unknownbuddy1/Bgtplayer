from pyrogram import Client, filters

from Bikash import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("donate")
    & filters.group)
async def donate(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/ceb0185c9bc67dce3ad3f.jpg",
        caption=f""" I Don't Need Money 💰 I Am Simple Script Chor If You Want Support Then Join Our Channel  [BACKUP](https://t.me/kissu123456) & Click Others Button And Join Our Channel..  [Movie-Bot](https://t.me/kissu_movies_bot)..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💐 support 💐", url=f"https://t.me/pwlived"
                    ),
                    InlineKeyboardButton(
                        "🦋Updates🦋", url=f"https://t.me/kissu123456")
                ]
            ]
        ),
    )
