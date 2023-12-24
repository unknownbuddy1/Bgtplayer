from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bikash import config
from Bikash import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🪺 Commands ",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ Bot Setting ⚙", callback_data="settings_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋 Channel 🦋", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="💐 Group 💐", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="🍿Movies-Bit🍿", url=f"https://t.me/kissu_movies_bot"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ADD TO GROUP 🥺 ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="HELP🎩", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋 Channel 🦋", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="💐 Group 💐", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="🍿Movies-Bot🍿", url=f"https://t.me/kissu_movies_bot"
            )
        ],
        [
            InlineKeyboardButton(
                text="𓆩•𝐊𝐢𝐬𝐬𝐮 💞•𓆪", user_id=OWNER
            )
        ]
     ]
    return buttons
