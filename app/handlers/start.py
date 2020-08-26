from telegram import *
from telegram.ext import *

from app.service import admin


def callback_start(update: Update, context: CallbackContext):
    user_telegram = update.message.from_user.id

    user = admin.user_get_or_create(user_telegram)
    update.message.reply_text(
        "hello"
    )


handlers = [
    CommandHandler('start', callback=callback_start)
]
