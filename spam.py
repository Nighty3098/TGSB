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
    return {proxy}


async def generate_user_data():
    global name, password, email, headers

    name = ""
    email = ""
    password = ""

    for i in range (10):
        name += choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        email += choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        password += choice("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")

    headers = {"User-Agent": generate_user_agent()}


async def start_sms_spam(phone, cycles):
    logger.info(f"Starting spam on {phone}")
    proxies = await generate_proxy()

    for i in range(0, cycles):
        await generate_user_data()
        logger.info(f"Generate new user agent: {headers}")
        logger.info(
            f"Generate new user data: name: {name}, password: {password}, email: {email}"
        )
        logger.info(f"Proxy: {await generate_proxy()}")

