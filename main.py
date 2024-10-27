#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from load import bot, dp
from aiogram import types
from FormaAdmin import *
from keyboard import*
from database import*
from config import*
from ChatForma import*
import asyncio
from traits import*
import time
from FormaAdmin import*
from model import *

generator = Generator()
btn = Button()
db = Database()




@dp.message_handler(commands=['start', 'go'])
async def start_handler(message: types.Message):
    print(message.from_user.id)
      
    #from datetime import datetime
    #fileId = "AgACAgIAAxkBAANcZwwL-emYUtwEKC8tOLtMa93tOnMAAqfoMRtMEGBILbrCi2y-dy4BAAMCAAN5AAM2BA"

    #user_id = message.from_user.id
    #user_name = f"@{message.from_user.username}"
    #time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #db.JustInsert(user_id, user_name, time_now)  
    
    await bot.send_message(
        message.from_user.id,
        text="""*Добро пожаловать в тех-поддержку WBS*""",
        parse_mode="Markdown",
        reply_markup=btn.menu()
    )

# 🖊 Добавить заведение
@dp.message_handler(commands=['robot'])
@dp.message_handler(Text(equals="Связоваться с ИИ 🤖 роботом"), content_types=['text'])
async def handler(message: types.Message):

    await Chat.waiting_for_message.set()

    await bot.send_message(
        message.from_user.id,
        text="""*Напишите проблему*""",
        parse_mode="Markdown",
        reply_markup=btn.cancel()
    )