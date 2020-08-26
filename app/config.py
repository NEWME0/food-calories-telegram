import os
import dotenv


DEBUG = True

dotenv.load_dotenv(verbose=DEBUG)

# Bot settings
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Webhook settings
WEBHOOK = {
    'HOST': '',
    'PORT': '',
    'PATH': '',
    'URL': '',
}

# Database settings
DATABASE = {
    'ENGINE': 'sqlite',
    'HOST': '',
    'PORT': '',
    'USER': '',
    'PASS': '',
    'NAME': 'food-calories-telegram',
}


BASE_URL = 'https://track-calorie.curs-valutar.xyz'
