import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
    "private bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_MSG = """Hey {}
i am Poisons Assistant 
You Can Contact My Master From Here
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('JOIN HERE', url= 'https://t.me/Team_Lad'),
        InlineKeyboardButton('SOURCE', url= 'https://github.com/Cat-of-tg/Private-bot')
        ]]
    )

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_MSG.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BTN
    )
Bot.run()
