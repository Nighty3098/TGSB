import random
import sys
from random import choice, randint
from threading import Thread

import requests
from requests import get, post
from user_agent import generate_user_agent

from spam.gen_user_data import gen_agents, gen_email, gen_password, gen_username
from spam.proxy import *
from spam.mask import *

sys.path.append("../")
from config import *


async def start_sms_spam(phone, cycles):
    for i in range(0, cycles):
        password = await gen_password()
        email = await gen_email()
        headers = await gen_agents()
        name = await gen_username()

        proxies = await generate_proxy()

        logger.debug(f"Generate new user agent: {headers}")
        logger.debug(
            f"Generate new user data: name: {name}, password: {password}, email: {email}"
        )
        logger.debug(f"Proxy: {await generate_proxy()}")


        phonee=mask(phone, "#(###)###-##-##")     
        logger.debug(f"Phone: {phonee}")
        phonee=mask(phone[:1], "+# (###) ###-##-##")     
        logger.debug(f"Phone: {phonee}")
        phonee=mask(phone[:1], "+# (###) ### - ## - ##")     
        logger.debug(f"Phone: {phonee}")