import os
import re
import sys

import loguru
import pretty_errors

from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher

# users role
# 0 - creator
# 1 - admin
# 2 - user
# 3 - don't access

home_dir = os.environ['HOME']
TOKEN = os.getenv("TGSB_TOKEN")
data_file = "data/data.json"
log_file = home_dir + "/logs/TGSB.log";
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