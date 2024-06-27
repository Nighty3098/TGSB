import os
import re
import sys

import loguru
import pretty_errors
import aiogram.enums 
import aiogram.filters 
import aiogram.types
import aiogram.utils.markdown 
from aiogram import * 

# users role
# 0 - создатель
# 1 - админ
# 2 - пользователь
# 3 - нет доступа


TOKEN = os.getenv("TGSB_TOKEN")
data_file = "data/data.json"
log_file = "logs/TGSB.log"
usernames = "data/names.txt"

bot = Bot(TOKEN)
dp = Dispatcher()

phone_pattern = re.compile(
    r"^(\+?7|8)?[-\s.]?(\d{3})[-\s.]?(\d{3})[-\s.]?(\d{2})[-\s.]?(\d{2})$"
)


logger = loguru.logger


logger.level("DEBUG", color="<green>")
logger.level("INFO", color="<cyan>")
logger.level("WARNING", color="<yellow>")
logger.level("CRITICAL", color="<red>")

logger.add(
    log_file,
    level="DEBUG",
    rotation="10000 MB",
    retention="7 days",
    backtrace=True,
    diagnose=True,
)

"""
logger.add(
    log_file,
    level="DEBUG",
    rotation="10000 MB",
    retention="7 days",
    format="{time: HH:mm:ss | YYYY-MM-DD} | {level} | {message} | ",
    backtrace=True,
    diagnose=True,
)
"""
