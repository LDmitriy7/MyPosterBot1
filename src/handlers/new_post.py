from telebot import on, ctx, bot, html

from assets import models, kbs, helpers, texts


@on.photo()
def _():
    helpers.process_media_group_photo()
    ctx.state = 'NewPost'

    helpers.send_post(models.Post.get())
    bot.send_message('В какой канал отправить?', kbs.Channels())


@on.text(state='NewPost')
def _():
    channel = models.Channel.find(title=ctx.text)

    if not channel:
        bot.send_message('Ошибка, выбери канал из списка')
        return

    channel.save(as_current=True)
    ctx.state = 'NewPost:publication_time'
    bot.send_message(texts.ask_publication_time, kbs.PublicationTime())


@on.text(kbs.PublicationTime.now, state='NewPost:publication_time')
def _(channel: models.Channel, post: models.Post):
    post_msg = helpers.publish_post(channel, post)  # TODO: safe
    text = html.a('Пост опубликован', helpers.get_url(post_msg))
    helpers.reset_ctx()
    bot.send_message(text, kbs.remove)


@on.text(state='NewPost:publication_time')
def _(channel: models.Channel, post: models.Post):
    try:
        publication_time = helpers.parse_datetime(ctx.text)
    except ValueError:
        bot.send_message(texts.invalid_publication_time)
        return

    helpers.publish_post(channel, post, at_time=publication_time)  # TODO: safe
    text = 'Пост запланирован на ' + html.b(publication_time)
    helpers.reset_ctx()
    bot.send_message(text, kbs.remove)
