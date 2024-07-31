import asyncio
import json
import logging
import sys

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

sys.path.append("../")
from config import logger, data_file, log_file, bot, TOKEN, phone_pattern, dp

async def admin_panel():
    try:
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text="💬 SMS spam (beta)", callback_data="sms_spam"))
        builder.add(
            types.InlineKeyboardButton(text="📞 Spam calls (in development)", callback_data="call_spam")
        )
        builder.adjust(1)

        logger.debug("Create admin panel")

        return builder.as_markup()
    except Exception as err:
        logger.error(f"{err}")
