import asyncio
import json
import logging

import psutil
import requests
from aiogram import *
from aiogram.enums import *
from aiogram.filters import *
from aiogram.types import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import *
from requests.models import *

from config import *
from MESSAGES_TEXT import *
from user_agents import *

# 0 - создатель
# 1 - админ
# 2 - пользователь
# 3 - нет доступа


async def check_user_id(user_id):
    with open(data_file, "r") as file:
        users_ids = json.load(file)

    if user_id in users_ids["developer"]:
        return 0
    elif user_id in users_ids["admins"]:
        return 1
    elif user_id in users_ids["id"]:
        return 2
    else:
        return 3


async def check_server():
    with open(data_file, "r") as file:
        data = json.load(file)

    if data["is_server_up"]:
        return True
    else:
        return False


@dp.message(CommandStart())
async def hello_message(message: Message) -> None:
    global user_id

    user_id = str(message.from_user.id)

    if await check_server():
        if await check_user_id(user_id) == 0:
            logger.info(f"Developer: {user_id} logged in")
            builder = InlineKeyboardBuilder()
            builder.add(
                types.InlineKeyboardButton(
                    text="Service control", callback_data="service_ctrl"
                )
            )

            await message.answer(HELLO_FOR_CREATOR, reply_markup=builder.as_markup())

        elif await check_user_id(user_id) == 1:
            logger.info(f"Admin: {user_id} logged in")
            await message.answer(HELLO_FOR_ADMIN)
        elif await check_user_id(user_id) == 2:
            logger.info(f"User: {user_id} started a bot")
            await message.answer(HELLO_FOR_USER)
        else:
            logger.warning(f"User: {user_id} not in whitelist")
            await message.answer(MESSAGE_FOR_NOT_IN_WHITELIST)

    else:
        if await check_user_id(user_id) == 0:
            logger.info(f"Developer: {user_id} logged in")
            await message.answer(HELLO_FOR_CREATOR)
        else:
            logger.warning("Server is not up")
            await message.answer(SERVER_IS_NOT_UP)


@dp.callback_query(F.data == "sys_stats")
async def system_stats(callback: types.CallbackQuery):
    if await check_user_id(user_id) == 0:
        logger.info(f"User: {user_id} open sys stats page")

        cpu_usage = str(psutil.cpu_percent(interval=None, percpu=False))
        memory_usage = str(psutil.virtual_memory().percent)

        message = f"CPU: {cpu_usage}%\nMemory: {memory_usage}%"
        await callback.message.answer(message)
    else:
        await callback.message.answer("У вас нет доступа к этой функции")
        logger.warning(f"User: {user_id} trying to open sys stats page")

@dp.callback_query(F.data == "service_ctrl")
async def service_ctrl(callback: types.CallbackQuery):
    if await check_user_id(user_id) == 0:
        logger.info(f"User: {user_id} open service ctrl page")
        with open(data_file, "r") as file:
            data = json.load(file)

        builder = InlineKeyboardBuilder()
        total_services = 60
        is_service_up = [data.get("is_server_up")]

        builder.add(types.InlineKeyboardButton(text="Sys stats", callback_data="sys_stats"))
        builder.add(
            types.InlineKeyboardButton(text="Whitelist", callback_data="echo_whitelist")
        )

        await callback.message.answer(
            f"------ SERVICE CONTROL ------\nis_service_up: {is_service_up}\ntotal_services: {total_services}\nTOKEN: {TOKEN} ",
            reply_markup=builder.as_markup(),
        )
    else:
        await callback.message.answer("У вас нет доступа к этой функции")
        logger.warning(f"User: {user_id} trying to open service ctrl page")

@dp.callback_query(F.data == "echo_whitelist")
async def echo_whitelist(callback: types.CallbackQuery):
    if await check_user_id(user_id) == 0:
        with open(data_file, "r") as f:
            whitelist = json.load(f)

        logger.info(f"User: {user_id} is looking at the whitelist")
        await callback.message.answer(str(json.dumps(whitelist, indent=2)))

    else:
        await callback.message.answer("У вас нет доступа к этой функции")
        logger.warning(f"User: {user_id} trying to looking at the whitelist")


@dp.message(Command("off"))
async def server_off(message: Message):
    if await check_user_id(user_id) == 0:
        with open(data_file, "r") as file:
            data = json.load(file)

        data["is_server_up"] = [data.get("is_server_up")]
        data["is_server_up"] = False

        with open(data_file, "w") as f:
            json.dump(data, f, indent=4)

        logger.critical(f"Server is down by {user_id}")
        await message.answer("Сервер отключен для всех, кроме создателя")
    else:
        logger.critical(f"{user_id} trying to stop server")
        await message.answer("У вас нет прав для этой команды")


@dp.message(Command("on"))
async def server_on(message: Message):
    if await check_user_id(user_id) == 0:
        with open(data_file, "r") as file:
            data = json.load(file)

        data["is_server_up"] = [data.get("is_server_up")]
        data["is_server_up"] = True

        with open(data_file, "w") as f:
            json.dump(data, f, indent=4)

        logger.critical(f"Server is up by {user_id}")
        await message.answer("Сервер включен для всех пользователей")
    else:
        logger.critical(f"{user_id} trying to start server")
        await message.answer("У вас нет прав для этой команды")


@dp.message(Command("adduser"))
async def add_in_whitelist(message: Message):
    if await check_user_id(user_id) == 1 or await check_user_id(user_id) == 0:
        pass
    else:
        logger.critical(f"{user_id} trying to add new user")
        await message.answer("У вас нет прав для этой команды")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
