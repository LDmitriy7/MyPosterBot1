from telebot import on, bot


@on.command('test', state='*')
def _():
    bot.send_message('?', chat_id=7244)
