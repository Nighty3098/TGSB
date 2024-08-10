import asyncio

from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher

from handlers import main_menu
from config import logger, data_file, log_file, bot, TOKEN, phone_pattern, dp


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
