import asyncio
import json
import logging
import sys

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

sys.path.append("../")
from config import *

async def admin_panel():
    try:
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(text="Смс спам (бета)", callback_data="sms_spam"))
        builder.add(
            types.InlineKeyboardButton(text="Спам звонками (в разработке)", callback_data="call_spam")
        )
        builder.adjust(1)

        logger.debug("Create admin panel")

        return builder.as_markup()
    except Exception as err:
        logger.error(f"{err}")
