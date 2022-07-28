from contextlib import suppress

from telebot import on, ctx, exc, bot

from assets import config


@on.message(state='*')
def check_access():
    if ctx.user_id not in config.admins_ids:
        raise exc.StopProcessing()


check_access.exclusive = False
check_access.check_first = True


@on.callback_query(state='*')
def answer_any():
    with suppress(exc.RequestError):
        bot.answer_callback_query()


answer_any.exclusive = False
answer_any.check_after_any = True
