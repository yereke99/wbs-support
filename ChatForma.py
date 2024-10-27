from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.message import Message
from load import dp, bot
from aiogram import types 
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import logging
from keyboard import*
from database import Database
import datetime
from main import*
import asyncio
from config import admin
from datetime import datetime
from traits import *
import time
from traits import*
from config import*
import os
from model import *

neuro = NeuroModel()

btn = Button()

@dp.message_handler(state='*', commands='⬅️ Выйти из чата')
@dp.message_handler(Text(equals='⬅️ Выйти из чата', ignore_case=True), state='*')
async def cancell_handler(message: types.Message, state: FSMContext):
    """
    :param message: Бастартылды
    :param state: Тоқтату
    :return: finish
    """
    
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Бас тарту!')

    async with state.proxy() as data:
        data['user_id'] = message.from_user.id
    
    await state.finish()
    await message.reply('⬅️ Вы вышли из чата', reply_markup=btn.menu())
        
    
class Chat(StatesGroup):
    waiting_for_message = State()
    

@dp.message_handler(state=Chat.waiting_for_message, content_types=types.ContentType.ANY)
async def handle_user_message(message: types.Message, state: FSMContext):
    
    
    async with state.proxy() as data:
        data['msg'] = message.text

    # тут используй свой модель для ответа

    response = neuro.chat(data['msg'])

    await bot.send_message(
        message.from_user.id,
        text=response,
        parse_mode="Markdown",
        reply_markup=btn.cancel()
    )

    await Chat.waiting_for_message.set()

