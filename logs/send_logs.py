import asyncio
import json
import logging
import re
import time

from aiogram.types import Message
from aiogram.types import FSInputFile
from aiogram.enums.chat_action import ChatAction

from config import bot, data_file, log_file, logger

async def send_log_to_dev():
    try:
        with open(data_file, "r") as file:
            users_ids = json.load(file)

        for DEV in users_ids["developer"]:
            file = FSInputFile(log_file, filename="TGSB.log")
            await bot.send_chat_action(chat_id=DEV, action=ChatAction.UPLOAD_DOCUMENT)
            await bot.send_document(chat_id=DEV, document=file, allow_sending_without_reply=True)
            logger.warning(f"Sending logs to dev: {DEV}")
    except Exception as err:
        logger.error(f"{err}")
