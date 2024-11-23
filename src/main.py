import asyncio

from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from setproctitle import setproctitle

from config import TOKEN, bot, data_file, dp, log_file, logger, phone_pattern
from handlers import main_menu


async def main() -> None:
    setproctitle("TGSB Service")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
