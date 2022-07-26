from groof import ctx, bot, html

import helpers
from assets import models, kbs, texts


def attach_photo():
    helpers.process_media_group_photo()
    helpers.has_any_channel()
    ctx.state = 'NewPost'
    helpers.send_post(models.Post.get())
    bot.send_message('В какой канал отправить?', kbs.Channels())


def attach_animation():
    models.Post(gif=ctx.file_id, caption=ctx.caption).save()
    helpers.has_any_channel()
    ctx.state = 'NewPost'
    helpers.send_post(models.Post.get())
    bot.send_message('В какой канал отправить?', kbs.Channels())


def save_channel():
    channel = models.Channel.find(chat_id=ctx.button['chat_id'])

    if not channel:  # TODO
        bot.send_message('Ошибка, выбери канал из списка')
        return

    channel.save(as_current=True)
    ctx.state = 'NewPost:publication_time'
    bot.edit_message_text(texts.ask_publication_time, kbs.PublicationTime())


def publish_post(channel: models.Channel, post: models.Post):
    post_msg = helpers.publish_post(channel, post)  # TODO: safe
    text = html.a('Пост опубликован', helpers.get_url(post_msg))
    helpers.reset_ctx()
    bot.edit_message_text(text)


def schedule_post(channel: models.Channel, post: models.Post):
    try:
        publication_time = helpers.parse_datetime(ctx.text)
    except ValueError:
        bot.send_message(texts.invalid_publication_time)
        return

    helpers.publish_post(channel, post, at_time=publication_time)  # TODO: safe
    text = 'Пост запланирован на ' + html.b(publication_time)
    helpers.reset_ctx()
    bot.send_message(text, kbs.remove)
