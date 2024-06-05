#!/usr/bin/env python3
# 8:43PM 2024-05-29
# ebiza.t.me
from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ChatJoinRequest
from info import ADMINS, REQ_CHANNEL_ONE, REQ_CHANNEL_TWO
from Script import script
from info import temp
from database.request_forcesub_db import add_req_one, add_req_two, is_requested_one, is_requested_two


# utils ---> 609, plugins.commands ---> 97
async def create_request_forcesub_buttons(user_id:int):
    btn = []
    if temp.LINK_ONE and user_id not in ADMINS and not await is_requested_one(user_id):
        btn.append([InlineKeyboardButton("🎗 Request To Join Channel 1 🎗", url=temp.LINK_ONE)])
    if temp.LINK_TWO and user_id not in ADMINS and not await is_requested_two(user_id):
        btn.append([InlineKeyboardButton("🎗 Request To Join Channel 2 🎗", url=temp.LINK_TWO)])
    if btn: return btn
  
@Client.on_chat_join_request(filters.chat(REQ_CHANNEL_ONE) | filters.chat(REQ_CHANNEL_TWO))
async def handle_join_request(bot: Client, join_req: ChatJoinRequest):
    if join_req.chat.id == REQ_CHANNEL_ONE:
        try: await add_req_one(join_req.from_user.id)
        except Exception as e: print(f"Error adding join request to req_one: {e}")
    elif join_req.chat.id == REQ_CHANNEL_TWO:
        try: await add_req_two(join_req.from_user.id)
        except Exception as e: return print(f"Error adding join request to req_two: {e}")