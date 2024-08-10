from config import logger

def mask(str, maska):
    try:
        if len(str) == maska.count('#'):
            str_list = list(str)
            for i in str_list:
                maska=maska.replace("#", i, 1)
        return maska
    except Exception as err:
        logger.error(f"{err}")

def format_phone(phone, phone_mask):
    phone_list = list(phone)
    for i in phone_list:
        phone_mask = phone_mask.replace("#", i, 1)
    return phone_mask

def parse_phone(phone):
    if len(phone) in [10, 11, 12]:
        if phone[0] == "+":
            phone = phone[1:]
        elif phone[0] == "8":
            phone = "7" + phone[1:]
        elif phone[0] == "9":
            phone = "7" + phone
        return phone
    else:
        logger.debug(f"Phone len: {len(phone)} not on [10, 11, 12]")