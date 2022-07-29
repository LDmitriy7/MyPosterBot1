import time
from datetime import datetime, timedelta

from telebot import ctx, bot, objects, exc
from . import models
from threading import Lock, Timer

lock = Lock()


def reset_ctx():
    ctx.state = None
    ctx.delete_current_models()
    ctx.data.clear()


def find_channel(title: str) -> models.Channel | None:
    for channel in models.Channel.get_collection():
        if channel.title == title:
            return channel


def send_post(
        post: models.Post,
        sign: str = None,
        sign_entities: list[objects.MessageEntity] = None,
        chat_id: int | str = None,
) -> objects.Message | list[objects.Message]:
    if len(post.photos) > 1:
        media = [objects.InputMediaPhoto(post.photos[0], caption=sign, caption_entities=sign_entities)]
        media += [objects.InputMediaPhoto(i) for i in post.photos[1:]]
        return bot.send_media_group(media, chat_id=chat_id)
    else:
        return bot.send_photo(post.photos[0], chat_id=chat_id, caption=sign, caption_entities=sign_entities)


def publish_post(
        channel: models.Channel,
        post: models.Post,
        at_time: datetime = None,
) -> objects.Message | list[objects.Message] | None:
    def send():
        return send_post(
            post,
            sign=channel.post_sign,
            sign_entities=channel.post_sign_entities,
            chat_id=channel.chat_id,
        )

    if at_time:
        delay = (at_time - datetime.now()).total_seconds()
        Timer(delay, send).start()
    else:
        return send()


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
        time.sleep(0.1)  # wait for other photos

    ctx.data['media_group_id'] = None


def update_post_sign(channel: models.Channel, text: str | None, entities: list[objects.MessageEntity]):
    channel.post_sign = text
    channel.post_sign_entities = entities
    channel.replace_in_collection(key='chat_id')
    bot.edit_message_reply_markup(message_id=ctx.data['request_msg_id'])
    reset_ctx()
    bot.send_message('Подпись обновлена')


def parse_datetime(text: str, now: datetime = None) -> datetime:
    now = now or datetime.now()
    raw_datetime = text.split(' ')
    raw_time = raw_datetime[-1]

    if len(raw_time) != 4:
        raise ValueError('Invalid time')

    hour = int(raw_time[:2].lstrip('0') or '0')
    minute = int(raw_time[2:4].lstrip('0') or '0')

    match len(raw_datetime):
        case 1:
            day = now.day
        case 2:
            day = int(raw_datetime[0])
        case _:
            raise ValueError('Invalid date')

    date = now.replace(day=day, hour=hour, minute=minute, second=0, microsecond=0)

    if date <= now:
        if date.day < now.day:
            if now.month == 12:
                date = date.replace(year=date.year + 1, month=1)
            else:
                date = date.replace(month=date.month + 1)
        else:
            date = date + timedelta(days=1)

    return date
