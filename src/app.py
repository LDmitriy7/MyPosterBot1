import logging

from telebot import run

import handlers
import middlewares
import tasks
from assets import logger

logging.basicConfig(level=30)

handlers.setup()
tasks.setup()
middlewares.setup()

logger.info("Starting up...")

run(
    parse_mode='html'
)
