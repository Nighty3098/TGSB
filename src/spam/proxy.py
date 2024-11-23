from random import choice, randint
from threading import Thread

import requests
from requests import get, post
from user_agent import generate_user_agent
from logs.send_logs import send_log_to_dev

async def generate_proxy():
    try:
        proxy = get(
            "https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true"
        ).text
        return {proxy}
    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()
