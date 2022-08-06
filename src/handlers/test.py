import helpers
from telebot import on

from assets import models


@on.command('test', state='*')
def _():
    channels = models.Channel.find_all()
    channel = models.Channel.find(chat_id=-1001500120189)

    print(channels)
    print(channel)
