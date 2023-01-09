import os
import logging
from dotenv import load_dotenv

load_dotenv()

# APPLICATION ENVIROMENT CONFIGURATION
APP_ENV = os.environ.get('APP_ENV', default='')


def ConfigEnv():
    if APP_ENV == 'DEV':
        return logging.DEBUG
    elif APP_ENV == 'PROD':
        return logging.WARNING
