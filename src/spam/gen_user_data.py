import random
from random import choice, randint
from threading import Thread

import requests
from requests import get, post
from user_agent import generate_user_agent

from config import logger, data_file, log_file, bot, TOKEN, phone_pattern, dp, usernames

async def gen_password():
    password = ""
    for _ in range(14):
        password += choice(
            "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        )

    return password


async def gen_agents():
    headers = generate_user_agent()

    return headers


async def gen_username():
    with open(usernames, "r") as f:
        names = [line.strip() for line in f]
    return random.choice(names)


async def gen_email():
    email = ""

    for _ in range(10):
        email += choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")

    email += "@gmail.com"

    return email
