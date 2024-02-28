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

    return builder.as_markup()
