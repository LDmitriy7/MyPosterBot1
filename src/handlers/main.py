from telebot import on, bot, ctx

from assets import kbs, models


@on.command('start', state='*')
def _():
    ctx.state = None
    bot.send_message('Отправь мне картинки')


@on.photo()
def _():
    models.Post(photos=[ctx.file_id]).save()
    bot.send_message('В какой канал отправить?', kbs.Channels())
    ctx.state = 'NewPost'
