from pyrogram import Client, filters

from Bikash import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("repo")
    & filters.group)
async def repo(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/ceb0185c9bc67dce3ad3f.jpg",
        caption=f"""☠️ I DON'T WANT TO SHOW SOURCE CODE 😭 SORRY BUT PLEASE SUPPORT ME  :
  [MOVIE-BOT](https://t.me/kissu_movies_bot)""",
        reply_markup=InlineKeyboardMarkup(
            [      
            [
                    InlineKeyboardButton(
                        "RENAMER-BOT", url=f"https://t.me/kissurenamerbot")
                ],
                [
                    InlineKeyboardButton(
                        "💐 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 💐", url=f"https://t.me/pwlivef"
                    ),
                    InlineKeyboardButton(
                        "🦋 UPDATES 🦋", url=f"https://t.me/kissu123456")
                ]
            ]
        ),
    ) 
