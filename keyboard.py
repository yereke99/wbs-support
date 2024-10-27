#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aiogram import types
import datetime
from load import bot
from database import Database

class Button:
    def __init__(self) -> None:
        pass

    def _create_keyboard(self, btns):

        button = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        for btn in btns:
            button.add(btn)

        return button
    
    def payment(self):

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("💳 Төлем жасау", url="https://pay.kaspi.kz/pay/0wdcrpat"))
        
        return keyboard
    
    def menu(self):

        k = ["Связоваться с ИИ 🤖 роботом"]

        return self._create_keyboard(k)
    

    def cancel(self):

        k = [
            "⬅️ Выйти из чата"
        ]

        return self._create_keyboard(k)
    
    # тут можно создать свой кнопки
    
    