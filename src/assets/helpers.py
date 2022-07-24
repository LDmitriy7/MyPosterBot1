import re
from datetime import datetime, timedelta
from threading import Timer

from telebot import ctx, bot, objects

from . import config, kbs, texts


def md_to_html(text: str):
    text = re.sub(r'\[(.+)]\((.+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'<a href="@(.+)">(.+)</a>', r'<a href="https://t.me/\1">\2</a>', text)
    return text


def publish_post(at_datetime: datetime = None):
    channel = ctx.data['channel']
    photos = ctx.data['photos']
    sign = ctx.data.get('sign')

    if sign:
        sign = md_to_html(sign)

    def _send():
        if len(photos) > 1:
            media = [objects.InputMediaPhoto(photos[0], caption=sign)]
            media += [objects.InputMediaPhoto(p) for p in photos[1:]]
            bot.send_media_group(media, chat_id=channel)
        else:
            bot.send_photo(photos[0], chat_id=channel, caption=sign)

    if at_datetime:
        delay = (at_datetime - datetime.now()).total_seconds()
        Timer(delay, _send).start()
        text = f'Пост запланирован на {at_datetime}'
    else:
        _send()
        text = 'Пост опубликован'

    bot.send_message(text, reply_markup=objects.ReplyKeyboardRemove())

    ctx.state = None
    ctx.data.clear()


def find_channel(username: str) -> config.Channel | None:
    for c in config.channels:
        if c.username == username:
            return c


def ask_publication_time():
    bot.send_message(texts.ask_publication_time, kbs.PublicationTime())
    ctx.state = 'NewPost:publication_time'


def parse_datetime(text: str) -> datetime:
    now = datetime.now()
    raw_datetime = text.split(' ')
    hour, minute = [int(i) for i in raw_datetime[-1].split(':')]

    match len(raw_datetime):
        case 1:
            day = now.day
        case 2:
            day = int(raw_datetime[0])
        case _:
            raise ValueError('Invalid datetime')

    date = now.replace(day=day, hour=hour, minute=minute, second=0, microsecond=0)

    if date < now:
        if date.day < now.day:
            if now.month == 12:
                date = date.replace(year=date.year + 1, month=1)
            else:
                date = date.replace(month=date.month + 1)
        else:
            date = date + timedelta(days=1)

    return date
