from assets import models
from telebot import on


@on.command('test', state='*')
def _():
    models.Channel(title='test').save(as_current=True)


@on.command('test2', state='*')
def _():
    print(models.Channel.current())
