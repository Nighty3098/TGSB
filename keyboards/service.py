import asyncio
import json
import logging
import sys

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


sys.path.append("../")
from config import logger, data_file, log_file, bot, TOKEN, phone_pattern, dp

async def service_panel():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="⚪ Sys stats", callback_data="sys_stats"))
    builder.add(types.InlineKeyboardButton(text="⚪ Give logs", callback_data="logs"))
    builder.add(types.InlineKeyboardButton(text="🟡 Clear logs", callback_data="rm_logs"))
    builder.add(types.InlineKeyboardButton(text="🔴 Off service", callback_data="off"))
    builder.add(types.InlineKeyboardButton(text="🟢 On service", callback_data="on"))
    builder.add(types.InlineKeyboardButton(text="  <<<  ", callback_data="menu"))
    builder.adjust(1)

    logger.debug("Create service panel")

    return builder.as_markup()
