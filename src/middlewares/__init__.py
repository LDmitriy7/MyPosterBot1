from groof import on

from .answer_any_query import answer_any_query


def setup():
    on.callback_query(state='*')(answer_any_query)
