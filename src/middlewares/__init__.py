from groof import Dispatcher

import events
from .answer_any_query import answer_any_query


def setup(dp: Dispatcher):
    dp.handle(events.any_query, answer_any_query)
