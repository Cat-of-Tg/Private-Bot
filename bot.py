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
ABOUT_MSG = """ 👀Source code
- owo it seems to great you have asked for source code. 
[CLICK here to get source code](https://github.com/Cat-of-Tg/Private-Bot). 
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('JOIN HERE', url= 'https://t.me/Team_Lad'),
        InlineKeyboardButton('SOURCE', callback_data='about') 
    )
ABOUT_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('JOIN HERE', callback_data='home'
    )

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_MSG.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BTN
    )

@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_MSG.format(update.from_user.mention),
            reply_markup=START_BTN,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_MSG,
            reply_markup=ABOUT_BTN,
            disable_web_page_preview=True
        )
    
Bot.run()
