from telebot import on, bot

import helpers
from assets import commands, kbs, models, texts, config


@on.start(state='*', user_id=config.admins_ids)
def _():
    commands.setup()
    start.func()


@on.start(state='*')
def start():
    helpers.reset_ctx()

    if not models.Channel.find():
        bot.send_message('Давай подключим твой первый канал')
        bot.send_message(texts.adding_channel_info)
    else:
        bot.send_message('Отправь мне пост', kbs.remove)


@on.command(commands.CANCEL, state='*')
@on.text(kbs.Cancel.button, state='*')
def _():
    helpers.reset_ctx()
    bot.send_message('Отменено', kbs.remove)
