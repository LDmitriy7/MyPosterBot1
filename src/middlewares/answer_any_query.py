from contextlib import suppress

from groof import exc, bot


def answer_any_query():
    with suppress(exc.RequestError):
        bot.answer_callback_query()


answer_any_query.exclusive = False
answer_any_query.check_after_any = True
