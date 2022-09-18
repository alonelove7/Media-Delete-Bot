#code by @nousername_psycho

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
import time
import random
import os
from os import getenv

#for heroku

api_id = int(getenv("API_ID", "13072738"))
api_hash = getenv("API_HASH", "64fae49dc49032fd6c6a3a97aa4d3156")
bot_token = getenv("BOT_TOKEN", "5417865081:AAGnnb06qgzA4GK1U5F8RCKez0duGKIbEQw")
g_time = int(getenv("GROUP_DELETE_TIME", "300"))
#for test 

# api_id = 1280226
# api_hash = '40c6be639fd3e699783cbb43c511cef0'
# bot_token = '1756158596:AAG3nIW1Nce_Uafvf10gejRR7bag0hw0edo'

admins = 5324263057
media_channel = -1001718732193 
bk_channel = -1001718732193



start_img = [
    "https://telegra.ph/file/f20d96bf6c083678a3de6.jpg"]

cyp = Client(
    'cyp_bot',
    api_id=api_id, 
    api_hash=api_hash, 
    bot_token=bot_token,
    sleep_threshold=60
)
print("bot starting")

@cyp.on_message(filters.command(['start']) & filters.private)
def start(client, message):
    message.reply_photo(photo=random.choice(start_img),
                        caption= "King_Network7",
                        reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton("Join Now",url="https://t.me/King_Network7")]])
                        )


@cyp.on_message(filters.photo | filters.video | filters.document)
def media_files(client, message):
    chat_id = message.chat.id
    video_id = message.message_id
    time.sleep(g_time)
    cyp.delete_messages(chat_id=chat_id, message_ids=video_id)
               
@cyp.on_message(filters.command('restart') & filters.group)
def  hrestart(client, message):
    user_id = message.from_user.id
    for member in cyp.get_chat_members(chat_id=message.chat.id, filter="administrators"):
        admin = member.user.id
        admins.append(admin)
    if user_id in admins: 
        msg = message.reply_text("Restarting ..")
        try:
            happ.restart()
            admins.clear()
        except Exception:
            msg.edit("failed to restart")
            admins.clear()
        
cyp.run()
