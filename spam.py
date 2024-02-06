from collections.abc import Coroutine
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes
import asyncio
import logging
import requests 
import threading

from config import *
from user_agents import *
from MESSAGES_TEXT import *

async def get_phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Coroutine:
    
