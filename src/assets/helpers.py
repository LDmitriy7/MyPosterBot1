import time

from telebot import ctx, bot, objects, exc
from . import models
from threading import Lock

lock = Lock()


def reset_ctx():
    ctx.state = None
    ctx.delete_current_models()
    ctx.data.clear()


def find_channel(title: str) -> models.Channel | None:
    for channel in models.Channel.get_collection():
        if channel.title == title:
            return channel


def send_post(post: models.Post, chat_id: int | str = None) -> objects.Message | list[objects.Message]:
    if len(post.photos) > 1:
        media = [objects.InputMediaPhoto(i) for i in post.photos]
        return bot.send_media_group(media, chat_id=chat_id)
    else:
        return bot.send_photo(post.photos[0], chat_id=chat_id)


def publish_post(channel: models.Channel, post: models.Post) -> objects.Message | list[objects.Message]:
    return send_post(post, channel.chat_id)


def get_url(post: objects.Message | list[objects.Message]):
    url = 'https://t.me'

    if isinstance(post, list):
        post = post[0]

    if post.chat.username:
        url += f'/{post.chat.username}'
    else:
        shift = -1_000_000_000_000
        url += f'/c/{shift - post.chat.id}'

    return url + f'/{post.message_id}'


def process_media_group_photo():
    lock.acquire()

    if ctx.data.get('media_group_id'):
        with models.Post.proxy() as post:
            post.photos.append(ctx.file_id)
        lock.release()
        raise exc.StopProcessing()

    models.Post(photos=[ctx.file_id]).save()

    ctx.data['media_group_id'] = ctx.media_group_id
    lock.release()

    if ctx.media_group_id:
        bot.send_chat_action('typing')
        time.sleep(1)  # wait for other photos

    ctx.data['media_group_id'] = None
