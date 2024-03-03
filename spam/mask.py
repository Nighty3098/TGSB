def mask(str, maska):
    if len(str) == maska.count('#'):
        str_list = list(str)
        for i in str_list:
            maska=maska.replace("#", i, 1)
    
    return maska