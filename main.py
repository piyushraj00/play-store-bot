# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Play-Store-Bot/blob/main/LICENSE

import os
import play_scraper
from pyrogram import Client, filters
from pyrogram.types import *


Bot = Client(
    "Play-Store-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@Bot.on_message(filters.private & filters.all)
async def filter_all(bot, update):
    text = "**Hi,\n\nIam A Simple Play Store Search Bot. I Can Search All From PlayStore. I Can Also Find App Details. Use Me Inline Made With ❤ BY @YouTubeVideoDownloaderService\n\n"
    reply_markup = InlineKeyboardMarkup(
        [
           [InlineKeyboardButton(text="♻️ Updates Channel", url: "https://t.me/YouTubeVideoDownloaderService")], [InlineKeyboardButton(text="⚜️ Search Here ⚜️", switch_inline_query_current_chat="")],
            [InlineKeyboardButton(text="🔷 Search In Another Chat 🔷", switch_inline_query="")]
        ]
    )
    await update.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_inline_query()
async def search(bot, update):
    results = play_scraper.search(update.query)
    answers = []
    for result in results:
        details = "**🔷 Title:** `{}`".format(result["title"]) + "\n" \
        "**♻️ Description:** `{}`".format(result["description"]) + "\n" \
        "**🖥️ App ID:** `{}`".format(result["app_id"]) + "\n" \
        "**⚜️ Developer:** `{}`".format(result["developer"]) + "\n" \
        "**👨🏻‍💻 Developer ID:** `{}`".format(result["developer_id"]) + "\n" \
        "**💯 Score:** `{}`".format(result["score"]) + "\n" \
        "**💰 Price:** `{}`".format(result["price"]) + "\n" \
        "**💲Full Price:** `{}`".format(result["full_price"]) + "\n" \
        "**🆓 Free:** `{}`".format(result["free"]) + "\n" \
        "\n" + " Made With ❤ BY @YouTubeVideoDownloaderService"
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Play Store", url="https://play.google.com"+result["url"])]]
        )
        try:
            answers.append(
                InlineQueryResultArticle(
                    title=result["title"],
                    description=result.get("description", None),
                    thumb_url=result.get("icon", None),
                    input_message_content=InputTextMessageContent(
                        message_text=details, disable_web_page_preview=True
                    ),
                    reply_markup=reply_markup
                )
            )
        except Exception as error:
            print(error)
    await update.answer(answers)


Bot.run()
