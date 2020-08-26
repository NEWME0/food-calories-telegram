import logging
import itertools

from telegram.ext import Updater

import app.config

from app.handlers import debug
from app.handlers import start


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # noqa
    level=logging.DEBUG
)


updater = Updater(
    token=app.config.BOT_TOKEN,
    use_context=True
)


# Set handlers here...
for handler in itertools.chain(
    start.handlers,
    debug.handlers,
):
    updater.dispatcher.add_handler(handler)


# Use polling if BOT_DEBUG is True
if app.config.DEBUG:
    updater.start_polling()
else:
    updater.start_webhook(
        listen=app.config.WEBHOOK['HOST'],
        port=app.config.WEBHOOK['PORT'],
        url_path=app.config.WEBHOOK['PATH'],
    )
    updater.bot.set_webhook(
        url=app.config.WEBHOOK['URL'],
    )


updater.idle()
