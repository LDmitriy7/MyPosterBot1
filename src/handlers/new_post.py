from telebot import on, ctx, bot, html, objects

from assets import models, kbs, helpers


@on.photo()
def _():
    helpers.process_media_group_photo()
    ctx.state = 'NewPost'
    helpers.send_post(models.Post.get())
    bot.send_message('В какой канал отправить?', kbs.Channels())


@on.text(state='NewPost')
def _(post: models.Post):
    channel = helpers.find_channel(ctx.text)

    if not channel:
        bot.send_message('Ошибка, выбери канал из списка')

    post_msg = helpers.publish_post(channel, post)  # TODO: safe
    text = html.a('Пост опубликован', helpers.get_url(post_msg))

    helpers.reset_ctx()
    bot.send_message(text, kbs.remove)
