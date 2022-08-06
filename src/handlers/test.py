import helpers
from telebot import on


@on.command('test', state='*')
def _():
    print(helpers.has_one_channel())
