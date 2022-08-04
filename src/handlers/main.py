from telebot import on, bot

from assets import helpers, commands, kbs


@on.start(state='*')
def _():
    helpers.reset_ctx()
    bot.send_message('Отправь мне пост', kbs.remove)


@on.command(commands.CANCEL, state='*')
@on.text(kbs.Cancel.button, state='*')
def _():
    helpers.reset_ctx()
    bot.send_message('Отменено', kbs.remove)


@on.command(commands.ADMIN, state='*')
def _():
    commands.setup()
    bot.send_message('Команды установлены')
