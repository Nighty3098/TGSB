import os
import sys
import pretty_errors
import loguru

from aiogram import *
from aiogram.enums import *
from aiogram.filters import *
from aiogram.types import *
from aiogram.utils.markdown import *
from loguru import *

TOKEN = os.getenv("TGSB_TOKEN")
data_file = "data.json"

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


logger = loguru.logger
logger.add("logs/TGSB.log", level="DEBUG", rotation="1000 MB", retention="7 days", format="{time} {level} {message}")
#logger.add(lambda msg: print(msg), level="DEBUG", format="{time} {level} {message}, serialize: True, backtrace=True, diagnose=True")
logger.level("INFO", color="<cyan>")
