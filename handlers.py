import asyncio
import json
import logging
import re

import psutil
import requests
from aiogram import *
from aiogram.enums import *
from aiogram.filters import *
from aiogram.filters import callback_data
from aiogram.types import *
from aiogram.types import message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import *
from requests.models import *

from config import *
from kb_builders import admin_panel, developer_panel, service_panel
from MESSAGES_TEXT import *
from spam import *
from user_agents import *
from validate import *


@dp.message(CommandStart())
async def main_menu(message: Message) -> None:
    global user_id

    user_id = str(message.from_user.id)

    if await check_server():
        if await check_user_id(user_id) == 0:
            logger.info(f"Developer: {user_id} logged in")

            await message.answer(
                HELLO_FOR_CREATOR, reply_markup=await developer_panel()
            )

        elif await check_user_id(user_id) == 1:
            logger.info(f"Admin: {user_id} logged in")

            await message.answer(HELLO_FOR_ADMIN, reply_markup=await admin_panel())

        elif await check_user_id(user_id) == 2:
            logger.info(f"User: {user_id} started a bot")
            await message.answer(HELLO_FOR_USER)
        else:
            logger.warning(f"User: {user_id} not in whitelist")
            await message.answer(MESSAGE_FOR_NOT_IN_WHITELIST)

    else:
        if await check_user_id(user_id) == 0:
            logger.info(f"Developer: {user_id} logged in")
            await message.answer(
                HELLO_FOR_CREATOR, reply_markup=await developer_panel()
            )
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
        await callback.message.answer(NO_ACCESS)
        logger.warning(f"User: {user_id} trying to open sys stats page")


@dp.callback_query(F.data == "service_ctrl")
async def service_ctrl(callback: types.CallbackQuery):
    if await check_user_id(user_id) == 0:
        logger.info(f"User: {user_id} open service ctrl page")
        with open(data_file, "r") as file:
            data = json.load(file)

        total_services = 60
        is_service_up = data.get("is_server_up")

        await callback.message.edit_text(
            f"           SERVICE CONTROL           \nis_service_up: {is_service_up}\ntotal_services: {total_services}\nTOKEN: {TOKEN} ",
            reply_markup=await service_panel(),
        )
    else:
        await callback.message.answer(NO_ACCESS)
        logger.warning(f"User: {user_id} trying to open service ctrl page")


@dp.callback_query(F.data == "menu")
async def menu(callback: types.CallbackQuery):
    # await main_menu(callback.message)
    await callback.message.edit_text(
        HELLO_FOR_CREATOR, reply_markup=await developer_panel()
    )


@dp.message(F.text, Command("whitelist"))
async def echo_whitelist(message: Message):
    if await check_user_id(user_id) == 0:
        with open(data_file, "r") as f:
            whitelist = json.load(f)

        logger.info(f"User: {user_id} is looking at the whitelist")
        await message.answer(str(json.dumps(whitelist, indent=2)))

    else:
        await message.answer(NO_ACCESS)
        logger.warning(f"User: {user_id} trying to looking at the whitelist")


@dp.callback_query(F.data == "logs")
async def send_logs(callback: types.CallbackQuery):
    if await check_user_id(user_id) == 0:
        await bot.send_document(user_id, log_file)

        logger.warning(f"Logs are sent to the user {user_id}")
    else:
        await callback.message.answer(NO_ACCESS)


@dp.callback_query(F.data == "rm_logs")
async def remove_logs(callback: types.CallbackQuery):
    logger.warning(f"{user_id} trying clear logs. ")
    if await check_user_id(user_id) == 0:
        try:
            os.remove(log_file)
            logger.info(f"{user_id} clear log")
            await callback.message.answer(DONE)
        except FileNotFoundError:
            logger.warning(f"log file not found ")
            await callback.message.answer(FILE_NOT_FOUND)
        else:
            await callback.message.answer(RM_LOG)
    else:
        logger.warning(f"{user_id} trying to clear logs")
        await callback.message.answer(NO_ACCESS)


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
        await message.answer(NO_ACCESS)


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
        await message.answer(NO_ACCESS)


@dp.message(Command("adduser"))
async def add_in_whitelist(message: Message):
    if await check_user_id(user_id) == 1 or await check_user_id(user_id) == 0:
        if message.text.startswith("/adduser"):
            new_user_id = str(message.text).split(" ")

            new_user_id = new_user_id[1]

            with open(data_file, "r") as f:
                data = json.load(f)

            data["id"].append(new_user_id)

            with open(data_file, "w") as f:
                json.dump(data, f, indent=4)

            logger.warning(f"{user_id} added new user {new_user_id}")
            await message.answer(f"Пользователь {new_user_id} добавлен в белый список")

        else:
            pass

    else:
        logger.critical(f"{user_id} trying to add new user")
        await message.answer(NO_ACCESS)


@dp.message(Command("removeuser"))
async def remove_from_whitelist(message: Message):
    if await check_user_id(user_id) == 1 or await check_user_id(user_id) == 0:
        if message.text.startswith("/removeuser"):
            rm_user_id = str(message.text).split(" ")

            rm_user_id = rm_user_id[1]

            with open(data_file, "r") as f:
                data = json.load(f)

            data["id"].remove(rm_user_id)

            with open(data_file, "w") as f:
                json.dump(data, f, indent=4)

            logger.warning(f"{user_id} removed user {rm_user_id}")
            await message.answer(f"Пользователь {rm_user_id} удалён из белого списка")

        else:
            pass

    else:
        logger.critical(f"{user_id} trying to remove user")
        await message.answer(NO_ACCESS)


@dp.message(Command("addadmin"))
async def add_in_admins(message: Message):
    if await check_user_id(user_id) == 1 or await check_user_id(user_id) == 0:
        if message.text.startswith("/addadmin"):
            new_admin_id = str(message.text).split(" ")

            new_admin_id = new_admin_id[1]

            with open(data_file, "r") as f:
                data = json.load(f)

            data["admins"].append(new_admin_id)

            with open(data_file, "w") as f:
                json.dump(data, f, indent=4)

            logger.warning(f"{user_id} added new admin {new_admin_id}")
            await message.answer(f"Пользователь {new_admin_id} добавлен в админку")

        else:
            pass

    else:
        logger.critical(f"{user_id} trying to add new admin")
        await message.answer(NO_ACCESS)


@dp.message(Command("removeadmin"))
async def remove_from_admins(message: Message):
    if await check_user_id(user_id) == 1 or await check_user_id(user_id) == 0:
        if message.text.startswith("/removeadmin"):
            rm_admin_id = str(message.text).split(" ")

            rm_admin_id = rm_admin_id[1]

            with open(data_file, "r") as f:
                data = json.load(f)

            data["admins"].remove(rm_admin_id)

            with open(data_file, "w") as f:
                json.dump(data, f, indent=4)

            logger.warning(f"{user_id} removed admin {rm_admin_id}")
            await message.answer(f"Пользователь {rm_admin_id} удалён из админов")

        else:
            pass

    else:
        logger.critical(f"{user_id} trying to remove admin")
        await message.answer(NO_ACCESS)


@dp.callback_query(F.data == "sms_spam")
async def get_phone_number(callback: types.CallbackQuery):
    await callback.message.edit_text("Введите номер телефона в формате 8XXXXXXXXXX")


@dp.message()
async def get_data_for_spam(message: Message):
    phone = message.text

    if phone_pattern.match(phone):
        logger.info(f"Client: {user_id} send phone number: {phone}")
        await message.answer(f"Введённый номер: {phone}\nНачинаю смс спам")
        await start_sms_spam(phone)
    else:
        await message.answer("Неправильный формат номера")
        await message.answer(HELLO_FOR_CREATOR, reply_markup=await developer_panel())
