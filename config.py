from telegram import *
from telegram.ext import *
import pretty_errors
import logging

TOKEN = os.getenv("TGSB_TOKEN")

admin = "1660218648"
whitelist_file = "whitelist.txt"

MAIN, MENU, CHECK_INPUT, ADMIN_INPUT, ADD_USER, REMOVE_USER, PRINT_WHITELIST = range(7)

app = ApplicationBuilder().token(TOKEN).build()
updater = Updater(TOKEN, app.update_queue)

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

logger = logging.getLogger(__name__)
