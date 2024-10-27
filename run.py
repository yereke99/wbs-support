from load import bot, storage
from main import dp
import asyncio
from database import Database
import datetime as dt
from keyboard  import*


db = Database()
btn = Button()


async def on_stop(dp):
    await bot.close()
    await storage.close()


def main():
    from aiogram import executor
    executor.start_polling(dp,  on_shutdown=on_stop)


if __name__ == "__main__":
    main()