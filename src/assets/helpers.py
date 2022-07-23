import re

from telebot import ctx, bot, objects

from . import config


def md_to_html(text: str):
    text = re.sub(r'\[(.+)]\((.+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'<a href="@(.+)">(.+)</a>', r'<a href="https://t.me/\1">\2</a>', text)
    return text


def publish_post():
    channel = ctx.data['channel']
    photos = ctx.data['photos']
    sign = ctx.data.get('sign')

    if sign:
        sign = md_to_html(sign)

    if len(photos) > 1:
        media = [objects.InputMediaPhoto(photos[0], caption=sign)]
        media += [objects.InputMediaPhoto(p) for p in photos[1:]]
        bot.send_media_group(media, chat_id=channel)
    else:
        bot.send_photo(photos[0], chat_id=channel, caption=sign)

    ctx.state = None
    ctx.data.clear()
    bot.send_message('Ок', reply_markup=objects.ReplyKeyboardRemove())


def find_channel(username: str) -> config.Channel | None:
    for c in config.channels:
        if c.username == username:
            return c
