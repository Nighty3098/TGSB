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
from keyboards.admin import *
from keyboards.dev import *
from keyboards.service import *
from keyboards.user import *
from MESSAGES_TEXT import *
from spam.spam import *
from validate import *


@dp.message(CommandStart())
async def main_menu(message: Message) -> None:
    try:
        global user_id

        user_id = str(message.from_user.id)
        chat_id = message.chat.id
        member = await bot.get_chat_member(chat_id, user_id)
        username = member.user.username

        msg = f"New user:{user_id}\n@{username}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=1660218648&text={msg}"
        logger.info((requests.get(url).json()))

        if await check_server():
            if await check_user_id(user_id) == 5:
                await message.answer(BLACKLIST)
            else:
                if await check_user_id(user_id) == 0:
                    logger.info(f"Developer: {user_id} logged in")
                    await message.answer_sticker(f'CAACAgIAAxkBAAEGTeRmdE-doD9AK-sKJTuZASJWoEH14QACvgUAAsEYngvKUihSmkk59jUE')
                    await message.answer(
                        HELLO_FOR_CREATOR, reply_markup=await developer_panel()
                    )

                elif await check_user_id(user_id) == 1:
                    logger.info(f"Admin: {user_id} logged in")
                    await message.answer_sticker(f'CAACAgIAAxkBAAEGTddmdE7rmfvBLTcZrvcsN-INxr7lGwACngUAAsEYngv9nvJaf3JwFzUE')
                    await message.answer(HELLO_FOR_ADMIN, reply_markup=await admin_panel())

                elif await check_user_id(user_id) == 2:
                    logger.info(f"User: {user_id} started a bot")
                    await message.answer_sticker(f'CAACAgIAAxkBAAEGTdtmdE79a_lU-0D0M1nDvXA-iV58fAACjgUAAsEYngt5UY-E655JgDUE')
                    await message.answer(HELLO_FOR_USER, reply_markup=await user_panel())
                else:
                    logger.warning(f"User: {user_id} not in whitelist")
                    await message.answer_sticker(f'CAACAgIAAxkBAAEGTd1mdE9CFw5gAnDwKvqtgqcQLFfkeAAC0AUAAsEYngtpgpEQVNsfsjUE')
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
    except Exception as err:
        logger.error(f"{err}")



@dp.callback_query(F.data == "sys_stats")
async def system_stats(callback: types.CallbackQuery):
    try:
        if await check_user_id(user_id) == 0:
            logger.debug(f"User: {user_id} open sys stats page")

            cpu_usage = str(psutil.cpu_percent(interval=None, percpu=False))
            memory_usage = str(psutil.virtual_memory().percent)

            message = f"CPU: {cpu_usage}%\nMemory: {memory_usage}%"
            await callback.message.answer(message)
        else:
            await callback.message.answer(NO_ACCESS)
            logger.warning(f"User: {user_id} trying to open sys stats page")
    except Exception as err:
        logger.error(f"{err}")



@dp.callback_query(F.data == "service_ctrl")
async def service_ctrl(callback: types.CallbackQuery):
    try:
        if await check_user_id(user_id) == 0:
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
    except Exception as err:
        logger.error(f"{err}")



@dp.callback_query(F.data == "menu")
async def menu(callback: types.CallbackQuery):
    try:
        # await main_menu(callback.message)
        await callback.message.edit_text(
            HELLO_FOR_CREATOR, reply_markup=await developer_panel()
        )
    except Exception as err:
        logger.error(f"{err}")



@dp.message(F.text, Command("whitelist"))
async def echo_whitelist(message: Message):
    try:
        if await check_user_id(user_id) == 0:
            with open(data_file, "r") as f:
                whitelist = json.load(f)

            logger.info(f"User: {user_id} is looking at the whitelist")
            await message.answer(str(json.dumps(whitelist, indent=2)))

        else:
            await message.answer(NO_ACCESS)
            logger.warning(f"User: {user_id} trying to looking at the whitelist")
    except Exception as err:
        logger.error(f"{err}")



@dp.callback_query(F.data == "logs")
async def send_logs(callback: types.CallbackQuery):
    try:
        if await check_user_id(user_id) == 0:
            file = FSInputFile(log_file, filename="logs.txt")
            await callback.message.edit_text("Sending logs...")
            await bot.send_chat_action(chat_id=user_id, action=ChatAction.UPLOAD_DOCUMENT)
            await bot.send_document(chat_id=user_id, document=file)

            logger.warning(f"Logs are sent to the user {user_id}")
        else:
            await callback.message.answer(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")



@dp.callback_query(F.data == "rm_logs")
async def remove_logs(callback: types.CallbackQuery):
    try:
        logger.warning(f"{user_id} trying clear logs. ")
        if await check_user_id(user_id) == 0:
            try:
                os.remove(log_file)
                logger.warning(f"{user_id} cleared log")
                await callback.message.answer(RM_LOG)
            except FileNotFoundError:
                logger.warning(f"log file not found ")
                await callback.message.answer(FILE_NOT_FOUND)
        else:
            logger.warning(f"{user_id} trying to clear logs")
            await callback.message.answer(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")


@dp.callback_query(F.data == "off")
async def server_off(callback: types.CallbackQuery):
    try:
        if await check_user_id(user_id) == 0:
            with open(data_file, "r") as file:
                data = json.load(file)

            data["is_server_up"] = [data.get("is_server_up")]
            data["is_server_up"] = False

            with open(data_file, "w") as f:
                json.dump(data, f, indent=4)

            logger.critical(f"Server is down by {user_id}")
            await callback.message.edit_text(
                "Сервер отключен для всех, кроме создателя",
                reply_markup=await developer_panel(),
            )
        else:
            logger.critical(f"{user_id} trying to stop server")
            await callback.message.edit_text(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")



@dp.callback_query(F.data == "on")
async def server_on(callback: types.CallbackQuery):
    try:
        if await check_user_id(user_id) == 0:
            with open(data_file, "r") as file:
                data = json.load(file)

            data["is_server_up"] = [data.get("is_server_up")]
            data["is_server_up"] = True

            with open(data_file, "w") as f:
                json.dump(data, f, indent=4)

            logger.critical(f"Server is up by {user_id}")
            await callback.message.edit_text(
                "Сервер включен для всех пользователей",
                reply_markup=await developer_panel(),
            )
        else:
            logger.critical(f"{user_id} trying to start server")
            await callback.message.edit_text(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")



@dp.message(Command("adduser"))
async def add_in_whitelist(message: Message):
    try:
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
    except Exception as err:
        logger.error(f"{err}")



@dp.message(Command("removeuser"))
async def remove_from_whitelist(message: Message):
    try:
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
    except Exception as err:
        logger.error(f"{err}")


@dp.message(Command("addadmin"))
async def add_in_admins(message: Message):
    try:
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
    except Exception as err:
        logger.error(f"{err}")



@dp.message(Command("removeadmin"))
async def remove_from_admins(message: Message):
    try:
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
    except Exception as err:
        logger.error(f"{err}")



@dp.message(Command("unblock"))
async def unblock_user(message: Message):
    try:
        if await check_user_id(user_id) == 1 or await check_user_id(user_id) == 0:
            if message.text.startswith("/unblock"):
                unblock_id = str(message.text).split(" ")

                unblock_id = unblock_id[1]

                with open(data_file, "r") as f:
                    data = json.load(f)

                data["blacklist"].remove(unblock_id)

                with open(data_file, "w") as f:
                    json.dump(data, f, indent=4)

                logger.warning(f"{user_id} unblocked {unblock_id}")
                await message.answer(f"Пользователь {unblock_id} разблокирован")

            else:
                pass

        else:
            logger.critical(f"{user_id} trying to remove admin")
            await message.answer(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")



@dp.message(Command("block"))
async def add_in_admins(message: Message):
    try:
        if await check_user_id(user_id) == 1 or await check_user_id(user_id) == 0:
            if message.text.startswith("/block"):
                block_id = str(message.text).split(" ")

                block_id = block_id[1]

                if await check_user_id(block_id) == 0:
                    await message.answer("Нельзя заблокировать разраба")
                else:
                    with open(data_file, "r") as f:
                        data = json.load(f)

                    data["blacklist"].append(block_id)

                    with open(data_file, "w") as f:
                        json.dump(data, f, indent=4)

                    logger.warning(f"{user_id} blocked {block_id}")
                    await message.answer(f"Пользователь {block_id} заблокирован")

            else:
                pass

        else:
            logger.critical(f"{user_id} trying to add new admin")
            await message.answer(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")



@dp.callback_query(F.data == "sms_spam")
async def get_phone_number(callback: types.CallbackQuery):
    await callback.message.edit_text(GET_PHONE)


@dp.message()
async def get_data_for_spam(message: Message):
    try:
        data = message.text
        data = data.split(" ")

        phone = str(data[0])
        phone = "7" + phone[1:]
        cycles = int(data[1])

        if phone_pattern.match(str(phone)):
            logger.info(
                f"Client: {user_id} send phone number: {phone}, cycles: {cycles}"
            )
            await message.answer(
                f"Введённый номер: {phone}\nКоличество кругов: {cycles}\nНачинаю смс спам"
            )
            await start_sms_spam(phone, cycles)
        else:
            await message.answer("Неправильный формат номера")
            await message.answer(
                HELLO_FOR_CREATOR, reply_markup=await developer_panel()
            )
    except Exception as err:
        logger.error(f"{err}")

    except IndexError as err:
        logger.error(err)
        await message.answer("Неправильный формат ввода\nПопробуйте заново")
