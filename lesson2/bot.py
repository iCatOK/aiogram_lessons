"""
In this chapter I practice text formating
in aiogram
"""

import asyncio
import logging
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.utils.formatting import as_marked_section, Bold, as_list, Italic
from dotenv import load_dotenv, find_dotenv

# logging config
logging.basicConfig(level=logging.INFO)

# load environment
load_dotenv(find_dotenv())

# config variables
token = os.environ.get('TOKEN')

# bot objects
bot = Bot(token=token, parse_mode=ParseMode.MARKDOWN_V2)
dp = Dispatcher()


# Если не указать фильтр F.text,
# то хэндлер сработает даже на картинку с подписью /test
@dp.message(F.text, Command("test"))
async def any_message(message: types.Message):
    await message.answer("Markdown answer\. Spoiler || HE IS BEHIND YOU WATCH OUT\!\!\! ||")


@dp.message(F.text, Command("report"))
async def report(message: types.Message):
    succeed_users = ["Забор Баранов", "Кормил Узбеков", "Курил Беломоров"]

    succeed_users_section = as_marked_section(
        Bold("Прошли испытание"),
        *succeed_users,
        marker='✅ '
    )
    failed_users_section = as_marked_section(
        Bold("Завалили испытание"),
        "Тугрик Агилев",
        marker='❌ '
    )

    content = as_list(
        Italic("Результаты испытания"),
        succeed_users_section,
        failed_users_section,
        sep="\n\n"
    )

    await message.answer(**content.as_kwargs())


@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("hewwo uwu!!!", parse_mode=None)


async def main():
    logging.info('Starting bot with markdown formatting by default')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

