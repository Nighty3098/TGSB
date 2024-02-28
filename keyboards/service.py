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


async def service_panel():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Sys stats", callback_data="sys_stats"))
    builder.add(types.InlineKeyboardButton(text="Give logs", callback_data="logs"))
    builder.add(types.InlineKeyboardButton(text="Clear logs", callback_data="rm_logs"))
    builder.add(types.InlineKeyboardButton(text="Off service", callback_data="off"))
    builder.add(types.InlineKeyboardButton(text="On service", callback_data="on"))
    builder.add(types.InlineKeyboardButton(text="  <<<  ", callback_data="menu"))
    builder.adjust(1)

    return builder.as_markup()
