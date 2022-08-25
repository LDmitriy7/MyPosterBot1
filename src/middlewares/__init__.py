from groof import Handler

import events
from .answer_any_query import answer_any_query

ALL = [
    Handler(events.any_query, answer_any_query),
]
