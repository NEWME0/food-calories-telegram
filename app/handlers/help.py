from telegram import *
from telegram.ext import *


def callback_help(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Food portion: \n'
        '/food_portion_list - description \n'
        '/food_portion_create - description \n'
        '/food_portion_retrieve - description \n'
        '/food_portion_update - description \n'
        '/food_portion_destroy - description \n'

        'Food category: \n'
        '/food_category_list - description \n'
        '/food_category_create - description \n'
        '/food_category_retrieve - description \n'
        '/food_category_update - description \n'
        '/food_category_destroy - description \n'

        'Food: \n'
        '/food_list - description \n'
        '/food_create - description \n'
        '/food_retrieve - description \n'
        '/food_update - description \n'
        '/food_destroy - description \n'

        'Activity: \n'
        '/activity_list - description \n'
        '/activity_create - description \n'
        '/activity_retrieve - description \n'
        '/activity_update - description \n'
        '/activity_destroy - description \n'

        'Food journal: \n'
        '/food_journal_list - description \n'
        '/food_journal_create - description \n'
        '/food_journal_retrieve - description \n'
        '/food_journal_update - description \n'
        '/food_journal_destroy - description \n'

        'Activity journal: \n'
        '/food_journal_list - description \n'
        '/food_journal_create - description \n'
        '/food_journal_retrieve - description \n'
        '/food_journal_update - description \n'
        '/food_journal_destroy - description \n'
        
        'Search: \n'
        '/search_food_category - description \n'
        '/search_food_portion - description \n'
        '/search_food - description \n'
        '/search_activity - description \n'
        '/search_journal_activity - description \n'
        '/search_journal_food - description \n'
        
        'Status: \n'
        '/status - description \n'
    )


handlers = [
    CommandHandler('help', callback=callback_help)
]
