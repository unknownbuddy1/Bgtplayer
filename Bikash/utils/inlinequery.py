from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="⏸️ Pause ⏸️",
            description=f"Pause Current Music.",
            thumb_url="https://graph.org/file/bde16770ca013669d8e00.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="⏹️ Resume ⏹️",
            description=f"Resume Music.",
            thumb_url="https://graph.org/file/ad0aa88b38a0c312547cb.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="⏩ 𝐒𝐤𝐢𝐩 ⏩",
            description=f"Skip And Play Nxt",
            thumb_url="https://graph.org/file/9020bdf0746e3c273900d.jpg",
            input_message_content=InputTextMessageContent("/skip", "/next"),
        ),
        InlineQueryResultArticle(
            title="📴 End 📴",
            description="End The Music.",
            thumb_url="https://graph.org/file/134ff623924c1ae44fe64.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🔉 Shuffle 🔉",
            description="shuffle Music .",
            thumb_url="https://graph.org/file/12483a2b8da9ca6e04e2a.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="🔈 Loop 🔈",
            description="Loop Music  .",
            thumb_url="https://graph.org/file/2b8a114bf2e63dc7ba32d.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
