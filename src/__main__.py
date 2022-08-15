import logging

import groof

import handlers
import jobs
import middlewares

logging.basicConfig(level=20, filename='.log', filemode='w')

handlers.setup()
middlewares.setup()
jobs.setup()

groof.run(parse_mode='html', disable_web_page_preview=True)
