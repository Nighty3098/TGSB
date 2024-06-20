def mask(str, maska):
    try:
        if len(str) == maska.count('#'):
            str_list = list(str)
            for i in str_list:
                maska=maska.replace("#", i, 1)
        return maska
    except Exception as err:
        logger.error(f"{err}")
