from telebot import on, bot

from assets import texts


@on.command('test', state='*')
def _():
    bot.send_message(texts.ask_publication_time)
