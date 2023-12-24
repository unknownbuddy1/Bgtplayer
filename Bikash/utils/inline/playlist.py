lfrom pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🤫 Personal 🤫",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="🌎 Global 🌏", callback_data="get_top_playlists"
            ),
        ],
        [           
            InlineKeyboardButton(
                text="🦋 Movies-Bot 🦋", url=f"https://t.me/kissu_movies_bot"
            ),
        ],
        [
            InlineKeyboardButton(
                text="☠️ Close ☠️", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Top-List", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="🤫 Personal 🤫", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="🌍 ɢʟᴏʙᴀʟ 🌏", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="💐 Group's 💐", callback_data="SERVERTOP chat"
            )
        ],
        [           
            InlineKeyboardButton(
                text="🍿Movies-Bot🍿", url=f"https://t.me/kissu_movies_bot"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁ Back ◁", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="☠️ Close ☠️", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Audio 🔊", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="Video 📽️", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁ Back ◁", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="☠️ Close ☠️", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Top-Playlist", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="🤫 Personal 🤫", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="🌏 Global 🌎", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="💐 Group'𝐬 💐", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="◁ Back ◁", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="☠️ Close ☠️", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="◁ Back ◁",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="☠️ Close ☠️", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🚫 𝐃𝐞𝐥𝐞𝐭𝐞 🚫",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="◁ 𝐁𝐚𝐜𝐤 ◁",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
