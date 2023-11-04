import asyncio
import logging
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv, find_dotenv

# logging config
logging.basicConfig(level=logging.INFO)

# load environment
load_dotenv(find_dotenv())

# config variables
token = os.environ.get('TOKEN')

# bot objects
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("hewwo uwu!!!")


@dp.message(Command("register"))
async def register_user(message: types.Message, users: set[str]):
    users.add(str(message.chat.id))
    await message.answer(f"Id пользователя зарегистрирован! ({message.chat.id})")


@dp.message(Command("info"))
async def register_user(message: types.Message, users: set[str]):
    users_str = "\n".join(users)
    await message.answer(f"Пользователи:\n{users_str}")


async def main():
    logging.info('Starting bot')
    dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    await dp.start_polling(bot, users=set())


if __name__ == '__main__':
    asyncio.run(main())

