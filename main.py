import asyncio

from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher

from handlers import *


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
