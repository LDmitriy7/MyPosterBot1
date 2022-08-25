import logging

import handlers
# import jobs
import middlewares
from assets import dp

logging.basicConfig(level=20, filename='.log', filemode='w')

dp.setup_handlers(handlers.ALL)
dp.setup_handlers(middlewares.ALL)
# dp.setup_jobs(jobs.ALL)

dp.run(parse_mode='html', disable_web_page_preview=True)
