from collections.abc import Coroutine
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes
import asyncio
import logging
import requests 
import threading

from config import *
from user_agents import *
from MESSAGES_TEXT import *

async def print_whitelist(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Coroutine:
    with open(whitelist_file, 'r') as file:
        await update.message.reply_text(file.read())
        
    return MAIN

async def add_in_whitelist(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Coroutine:
    user_id = str(update.effective_user.id)
    with open(whitelist_file, 'a') as file:
        file.write(f"{user_id}\n")
        logger.info(msg=user_id)
        logger.info(msg="User added to whitelist")



async def check_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE, user_id) -> Coroutine:
    with open(whitelist_file, 'r') as file:
        if user_id in file.read():
            return True
        else:
            return False 
       

async def check_user_input(update: Update, context: MessageHandler) -> Coroutine:
    check = MessageHandler.check_update(update, context)
    user_message = update.message.text

    if user_message == "Спам смс":
        logger.info(msg="User: " + update.effective_user.first_name + " started sms spam")
        return SMS_SPAM 
    elif user_message == "Спам звонками":
        logger.info(msg="User: " + update.effective_user.first_name + " started call spam")
        return CALL_SPAM


async def check_admin_input(update: Update, context: MessageHandler) -> Coroutine:
    check = MessageHandler.check_update(update, context)
    user_message = update.message.text

    if user_message == "Спам смс":
        logger.info(msg="Admin: " + update.effective_user.first_name + " started sms spam")
        return SMS_SPAM 
    elif user_message == "Спам звонками":
        logger.info(msg="Admin: " + update.effective_user.first_name + " started call spam")
        return CALL_SPAM
    elif user_message == "Добавить в whitelist":
        logger.info(msg="Admin: " + update.effective_user.first_name + " added user to whitelist")
        return ADD_USER
    elif user_message == "Удалить из whitelist":
        logger.info(msg="Admin: " + update.effective_user.first_name + " removed user from whitelist")
        return REMOVE_USER
    elif user_message == "Вывести whitelist":
        logger.info(msg="Admin: " + update.effective_user.first_name + " showed whitelist")
        await print_whitelist(update, context)
        #return PRINT_WHITELIST


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Coroutine:
    threading.Thread(target=shutdown).start()


async def hello_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = str(update.effective_user.id)

    if await check_user_id(update, context, user_id) :
        if user_id == admin:
            await update.message.reply_text("Добро пожаловать, админ")

            logger.info(msg=update.message.chat.id)
            logger.info(msg="Admin logged in")

            admin_menu = [["Спам смс", "Спам звонками"], ["Добавить в whitelist"], ["Удалить из whitelist"], ["Вывести whitelist"]]
            await update.message.reply_text(
                "Выберите нужный пункт: ",
                reply_markup=ReplyKeyboardMarkup(
                    admin_menu, one_time_keyboard=False, resize_keyboard=True
                ),
            )

            return ADMIN_INPUT

        else:
            await update.message.reply_text(f'Привет {update.effective_user.first_name}')

            logger.info(msg=update.message.chat.id)
            logger.info(msg="User in WHITELIST")

            main_menu = [["Спам смс", "Спам звонками"]]
            await update.message.reply_text(
                "Выберите нужный пункт: ",
                reply_markup=ReplyKeyboardMarkup(
                    main_menu, one_time_keyboard=False, resize_keyboard=True
                ),
            )

            return CHECK_INPUT

    else :
        logger.warning(msg=update.message.chat.id)
        logger.warning(msg="User not in WHITELIST")

        await update.message.reply_text("Вы не находитесь в белом списке. Для добавления обратитесь к администратору: @Night3098")


def main():
    conv_handler = ConversationHandler(
        per_message=False,
        entry_points=[
            CommandHandler("start", hello_message),
        ],
        states={
            MAIN: [CallbackQueryHandler(hello_message)],
            MENU: [CommandHandler("stop", stop)],
            PRINT_WHITELIST: [CallbackQueryHandler(print_whitelist)],
            CHECK_INPUT: [MessageHandler(filters.TEXT & (~filters.COMMAND), check_user_input)],
            ADMIN_INPUT: [MessageHandler(filters.TEXT & (~filters.COMMAND), check_admin_input)],
        },
        fallbacks=[CommandHandler("stop", stop)],
    )

    app.add_handler(conv_handler)

    app.run_polling(allowed_updates=Update.ALL_TYPES)

asyncio.run(main())

