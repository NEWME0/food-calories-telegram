import logging
import itertools

from telegram.ext import Updater

import app.config

from app.handlers import start
from app.handlers import help
from app.handlers import debug

# Init logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # noqa
    level=logging.DEBUG
)

# Init bot
updater = Updater(
    token=app.config.BOT_TOKEN,
    use_context=True
)


# Here we register handlers
for handler in itertools.chain(
    start.handlers,
    help.handlers,
    debug.handlers,
):
    updater.dispatcher.add_handler(handler)


# Use polling if DEBUG is True
# Or webhook if DEBUG is False
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
