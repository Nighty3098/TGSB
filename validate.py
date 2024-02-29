import asyncio
import json

from config import *


async def check_user_id(user_id):
    with open(data_file, "r") as file:
        users_ids = json.load(file)

    if user_id in users_ids["blacklist"]:
        return 5
    if user_id in users_ids["developer"]:
        return 0
    elif user_id in users_ids["admins"]:
        return 1
    elif user_id in users_ids["id"]:
        return 2
    else:
        return 3


async def check_server():
    with open(data_file, "r") as file:
        data = json.load(file)

    if data["is_server_up"]:
        return True
    else:
        return False
