from telebot import on

from assets import models


@on.command('test', state='*')
def _(post: models.Post):
    print(post)
