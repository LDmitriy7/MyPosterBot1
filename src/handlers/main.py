from telebot import on, bot, ctx

from assets import kbs


@on.command('start', state='*')
def _():
    ctx.state = None
    bot.send_message('Отправь мне картинки')


@on.photo()
def _():
    ctx.data.clear()
    ctx.data['photos'] = [ctx.file_id]
    bot.send_message('В какой канал отправить?', kbs.Channels())
    ctx.state = 'NewPost'
