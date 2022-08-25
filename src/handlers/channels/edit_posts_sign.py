from groof import bot, ctx

import helpers
from assets import kbs, models


def ask_channel():
    helpers.has_any_channel()
    ctx.state = 'Channels'
    bot.send_message('Выбери канал для редактирования', reply_markup=kbs.Channels())


def ask_new():
    channel = models.Channel.find(chat_id=ctx.button['chat_id'])

    if not channel:  # TODO
        bot.send_message('Ошибка, выбери канал из списка')
        return

    channel.save(as_current=True)

    ctx.state = 'Channels:sign'
    msg = bot.edit_message_text('Отправь новую подпись для постов в канале', kbs.EditSign())
    ctx.data['request_msg_id'] = msg.message_id


def ask_channel_from_list():
    bot.send_message('Ошибка, выбери канал из списка')


def set_empty_post_sign(channel: models.Channel):
    helpers.update_post_sign(channel, text=None, entities=[])


def cancel_editing_sign():
    helpers.reset_ctx()
    bot.edit_message_text('Отменено')


def set_new(channel: models.Channel):
    helpers.update_post_sign(channel, ctx.text, ctx.message.entities)
