#code by @nousername_psycho

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
import time
import random
import os
from os import getenv
import heroku3

#for heroku

api_id = int(getenv("API_ID"))
api_hash = getenv("API_HASH")
bot_token = getenv("BOT_TOKEN")
g_time = int(getenv("GROUP_DELETE_TIME"))
#for test 

# api_id = 1280226
# api_hash = '40c6be639fd3e699783cbb43c511cef0'
# bot_token = '1756158596:AAG3nIW1Nce_Uafvf10gejRR7bag0hw0edo'

admins = [5324263057]
media_channel = -1001718732193 
bk_channel = -1001718732193

heroku_conn = heroku3.from_key('e4a927b1-9480-4432-9b6b-b9c9bc4783ba')
happ = heroku_conn.apps()['adholokham100']


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
