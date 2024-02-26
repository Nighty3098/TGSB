from random import choice, randint
from threading import Thread

import requests
from requests import get, post
from user_agent import generate_user_agent

from config import *
from handlers import *


async def generate_proxy():
    proxy = get(
        "https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true"
    ).text
    return {"http": proxy, "https": proxy}


async def generate_user_data():
    global name, password, email, headers
    name = ""
    for _ in range(12):
        name += choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        password = name + choice(
            "123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        )
        email = (
            name
            + choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
            + "@gmail.com"
        )

    headers = {"User-Agent": generate_user_agent()}


async def start_sms_spam(phone_number):
    logger.info(f"Starting spam on {phone_number}")

    for i in range(1, 10):
        await generate_user_data()
        logger.info(f"Generate new user agent: {headers}")
        logger.info(
            f"Generate new user data: name: {name}, password: {password}, email: {email}"
        )
        logger.info(f"Proxy: {await generate_proxy()}")
