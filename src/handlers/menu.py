from groof import bot

import helpers
from assets import commands, kbs, models, texts


def on_start():
    helpers.reset_ctx()

    if not models.Channel.find():
        bot.send_message('Давай подключим твой первый канал')
        bot.send_message(texts.adding_channel_info)
    else:
        bot.send_message('Отправь мне пост', kbs.remove)


def on_start_by_admin():
    commands.setup()
    on_start()


def cancel():
    helpers.reset_ctx()
    bot.send_message('Отменено', kbs.remove)
