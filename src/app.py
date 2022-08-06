import logging

from telebot import run

import handlers
import middlewares
import tasks

logging.basicConfig(level=20, filename='.log', filemode='w')

handlers.setup()
tasks.setup()
middlewares.setup()

run(parse_mode='html', disable_web_page_preview=True)
