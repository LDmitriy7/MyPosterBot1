from telebot import on, bot, objects

from assets import commands, config


@on.command(commands.LOGS, state='*', user_id=config.admins_ids)
def _():
    bot.send_document(objects.InputFile('.log', 'logs.txt'))
