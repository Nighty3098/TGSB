import asyncio
import json
import logging
import sys

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

sys.path.append("../")
from config import logger, data_file, log_file, bot, TOKEN, phone_pattern, dp


async def user_panel():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="💬 SMS spam (in development)", callback_data="sms_spam"))
    builder.add(
        types.InlineKeyboardButton(text="📞 Spam calls (in development)", callback_data="call_spam")
    )
    builder.adjust(1)

    logger.debug("Create user panel")

    return builder.as_markup()
