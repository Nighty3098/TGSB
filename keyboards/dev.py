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


async def developer_panel():
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text="🚀 Service management", callback_data="service_ctrl"
        )
    )
    builder.add(types.InlineKeyboardButton(text="💬 SMS spam (beta)", callback_data="sms_spam"))
    builder.add(
        types.InlineKeyboardButton(text="📞 Spam calls (in development)", callback_data="call_spam")
    )
    builder.adjust(1)

    logger.debug("Create developer panel")

    return builder.as_markup()
