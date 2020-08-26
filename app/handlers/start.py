from telegram import *
from telegram.ext import *

from app.wrappers.user import User


def callback_start(update: Update, context: CallbackContext):
    user_telegram = update.message.from_user.id
    user = User(user_telegram)

    update.message.reply_text(
        "hello"
    )


handlers = [
    CommandHandler('start', callback=callback_start)
]
