import logging

import handlers
import jobs
import middlewares
from assets import dp

logging.basicConfig(level=20, filename='.log', filemode='w')

handlers.setup(dp)
middlewares.setup(dp)
jobs.setup(dp)

dp.run(parse_mode='html', disable_web_page_preview=True)
