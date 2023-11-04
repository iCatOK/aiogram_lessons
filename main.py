import asyncio
import logging
import os

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


async def main():
    logging.info('Starting bot')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

