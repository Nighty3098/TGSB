from random import choice, randint
from threading import Thread

import requests
from requests import get, post
from user_agent import generate_user_agent


async def generate_proxy():
    proxy = get(
        "https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true"
    ).text
    return {proxy}
