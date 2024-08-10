import asyncio
import json
import logging
import re

import psutil
import requests

from aiogram import handlers, F, types
from aiogram.types import Message
from aiogram.filters import CommandStart, Filter, Command
from aiogram.types.input_file import InputFile
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext

from config import logger, data_file, log_file, bot, TOKEN, phone_pattern, dp
from keyboards.admin import admin_panel
from keyboards.dev import developer_panel
from keyboards.service import service_panel
from keyboards.user import user_panel
from MESSAGES_TEXT import HELLO_FOR_ADMIN, HELLO_FOR_CREATOR, HELLO_FOR_USER, MESSAGE_FOR_NOT_IN_WHITELIST, SERVER_IS_NOT_UP, NO_ACCESS, FILE_NOT_FOUND, DONE, RM_LOG, GET_PHONE, BLACKLIST, SMS_ERR, SPAM_DONE
from spam.spam import start_sms_spam
from spam.mask import mask, parse_phone, format_phone
from validate import check_server, check_user_id
from logs.send_logs import send_log_to_dev

@dp.message(CommandStart())
async def main_menu(message: Message) -> None:
    try:
        global user_id

        user_id = str(message.from_user.id)
        chat_id = message.chat.id
        member = await bot.get_chat_member(chat_id, user_id)
        username = member.user.username

        image_path = 'data/header.png'

        msg = f"New user:{user_id}\n@{username}"
        await bot.send_message(1660218648, msg, allow_sending_without_reply=True)

        if await check_server():
            if await check_user_id(user_id) == 5:
                await message.answer(BLACKLIST)
            else:
                if await check_user_id(user_id) == 0:
                    logger.info(f"Developer: {user_id} logged in")

                    photo = FSInputFile(image_path)
                    await message.answer_photo(photo, caption=HELLO_FOR_CREATOR, reply_markup=await developer_panel())

                elif await check_user_id(user_id) == 1:
                    logger.info(f"Admin: {user_id} logged in")

                    photo = FSInputFile(image_path)
                    await message.answer_photo(photo, caption=HELLO_FOR_ADMIN, reply_markup=await admin_panel())

                elif await check_user_id(user_id) == 2:
                    photo = FSInputFile(image_path)
                    await message.answer_photo(photo, caption=HELLO_FOR_USER, reply_markup=await user_panel())

                    logger.info(f"User: {user_id} started a bot")
                else:
                    logger.warning(f"User: {user_id} not in whitelist")
                    image_path2 = 'data/ban.png'
                    photo2 = FSInputFile(image_path2)
                    await message.answer_photo(photo2, caption=MESSAGE_FOR_NOT_IN_WHITELIST)


        else:
            if await check_user_id(user_id) == 0:
                logger.info(f"Developer: {user_id} logged in")

                photo = FSInputFile(image_path)
                await message.answer_photo(photo, caption=HELLO_FOR_CREATOR, reply_markup=await developer_panel())
            else:
                logger.warning("Server is not up")
                await message.answer(SERVER_IS_NOT_UP)
        
        await send_log_to_dev()
    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()



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
        await send_log_to_dev()




@dp.callback_query(F.data == "service_ctrl")
async def service_ctrl(callback: types.CallbackQuery):
    try:
        if await check_user_id(user_id) == 0:
            with open(data_file, "r") as file:
                data = json.load(file)

            total_services = 60
            is_service_up = data.get("is_server_up")

            message_id = callback.message.message_id

            await bot.edit_message_caption(chat_id=callback.message.chat.id, message_id=message_id, caption=
            f"           SERVICE CONTROL           \nis_service_up: {is_service_up}\ntotal_services: {total_services}\nTOKEN: {TOKEN} ",
                reply_markup=await service_panel(),
            )
        else:
            await callback.message.answer(NO_ACCESS)
            logger.warning(f"User: {user_id} trying to open service ctrl page")
    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()




@dp.callback_query(F.data == "menu")
async def menu(callback: types.CallbackQuery):
    try:
        message_id = callback.message.message_id

        await bot.edit_message_caption(chat_id=callback.message.chat.id, message_id=message_id, caption=HELLO_FOR_CREATOR, reply_markup=await developer_panel())

    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()



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
        await send_log_to_dev()



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
        await send_log_to_dev()



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
                logger.warning("log file not found ")
                await callback.message.answer(FILE_NOT_FOUND)
        else:
            logger.warning(f"{user_id} trying to clear logs")
            await callback.message.answer(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()


@dp.callback_query(F.data == "off")
async def server_off(callback: types.CallbackQuery):
    try:
        if await check_user_id(user_id) == 0:
            with open(data_file, "r") as file:
                data = json.load(file)

            data["is_server_up"] = False

            with open(data_file, "w") as f:
                json.dump(data, f, indent=4)

            logger.critical(f"Server is down by {user_id}")
            await callback.message.answer("The server is disabled for everyone except the creator\n\n")
        else:
            logger.critical(f"{user_id} trying to stop server")
            await callback.message.answer(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()



@dp.callback_query(F.data == "on")
async def server_on(callback: types.CallbackQuery):
    try:
        if await check_user_id(user_id) == 0:
            with open(data_file, "r") as file:
                data = json.load(file)

            data["is_server_up"] = True

            with open(data_file, "w") as f:
                json.dump(data, f, indent=4)

            logger.critical(f"Server is up by {user_id}")
            await callback.message.answer("Server enabled for all users\n\n")
        else:
            logger.critical(f"{user_id} trying to start server")
            await callback.message.answer(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()



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
                await message.answer(f"User {new_user_id} has been added to the whitelist")

        else:
            logger.critical(f"{user_id} trying to add new user")
            await message.answer(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()



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
                await message.answer(f"User {rm_user_id} has been removed from the whitelist")

        else:
            logger.critical(f"{user_id} trying to remove user")
            await message.answer(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()


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
                await message.answer(f"User {new_admin_id} added to the admin area")

        else:
            logger.critical(f"{user_id} trying to add new admin")
            await message.answer(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()



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
                await message.answer(f"User {rm_admin_id} has been removed from admins")

        else:
            logger.critical(f"{user_id} trying to remove admin")
            await message.answer(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()



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
                await message.answer(f"User {unblock_id} unblocked")

        else:
            logger.critical(f"{user_id} trying to remove admin")
            await message.answer(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()



@dp.message(Command("block"))
async def add_in_admins(message: Message):
    try:
        if await check_user_id(user_id) == 1 or await check_user_id(user_id) == 0:
            if message.text.startswith("/block"):
                block_id = str(message.text).split(" ")

                block_id = block_id[1]

                if await check_user_id(block_id) == 0:
                    await message.answer("You can't block the dev")
                else:
                    with open(data_file, "r") as f:
                        data = json.load(f)

                    data["blacklist"].append(block_id)

                    with open(data_file, "w") as f:
                        json.dump(data, f, indent=4)

                    logger.warning(f"{user_id} blocked {block_id}")
                    await message.answer(f"User {block_id} is blocked")

        else:
            logger.critical(f"{user_id} trying to add new admin")
            await message.answer(NO_ACCESS)
    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()



@dp.callback_query(F.data == "sms_spam")
async def get_phone_number(callback: types.CallbackQuery):
    message_id = callback.message.message_id
    await bot.edit_message_caption(chat_id=callback.message.chat.id, message_id=message_id, caption=GET_PHONE)


@dp.message()
async def get_data_for_spam(message: Message):
    try:
        data = message.text
        data = data.split(" ")

        phone = parse_phone(str(data[0]))
        cycles = int(data[1])

        if phone_pattern.match(str(phone)):
            logger.info(
                f"Client: {user_id} send phone number: {phone}, cycles: {cycles}"
            )
            await message.answer(
                f"🟢 Number entered: {phone}\n🟢 Number of laps: {cycles}\n✅ I'm going to start texting."
            )
            await start_sms_spam(phone, cycles)
            await message.answer(SPAM_DONE)
        else:
            await message.answer(" ❌ Incorrect number format ❌ ")
            await main_menu(message)

    except IndexError as err :
        logger.error(f"{err}")
        await message.answer(" ❌ Incorrect input format. Try again ❌ ")
    except Exception as err :
        logger.error(f"{err}")
        await send_log_to_dev()