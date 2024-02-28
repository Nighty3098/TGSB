import asyncio
import json
import logging

import psutil
import requests
from aiogram import *
from aiogram.enums import *
from aiogram.filters import *
from aiogram.filters import callback_data
from aiogram.types import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import *
from requests.models import *

from config import *
from MESSAGES_TEXT import *
from validate import *


async def developer_panel():
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text="Управление сервисом", callback_data="service_ctrl"
        )
    )
    builder.add(types.InlineKeyboardButton(text="Смс спам", callback_data="sms_spam"))
    builder.add(
        types.InlineKeyboardButton(text="Спам звонками", callback_data="call_spam")
    )
    builder.adjust(1)

    logger.debug("Creating developer panel")

    return builder.as_markup()


async def admin_panel():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Смс спам", callback_data="sms_spam"))
    builder.add(
        types.InlineKeyboardButton(text="Спам звонками", callback_data="call_spam")
    )
    builder.adjust(1)

    logger.debug("Creating admin panel")

    return builder.as_markup()


async def service_panel():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Sys stats", callback_data="sys_stats"))
    builder.add(types.InlineKeyboardButton(text="Give logs", callback_data="logs"))
    builder.add(types.InlineKeyboardButton(text="Clear logs", callback_data="rm_logs"))
    builder.add(types.InlineKeyboardButton(text="Off service", callback_data="off"))
    builder.add(types.InlineKeyboardButton(text="On service", callback_data="on"))
    builder.add(types.InlineKeyboardButton(text="  <<<  ", callback_data="menu"))
    builder.adjust(1)

    logger.debug("Creating service panel")

    return builder.as_markup()
