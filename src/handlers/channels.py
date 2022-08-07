from telebot import on, bot, ctx

import helpers
from assets import commands, kbs, models


@on.command(commands.CHANNELS)
def _():
    helpers.has_any_channel()
    ctx.state = 'Channels'
    msg = bot.send_message('Выбери канал для редактирования', reply_markup=kbs.Channels())


@on.button(kbs.Channels.channel, state='Channels')
def _():
    channel = models.Channel.find(chat_id=ctx.button['chat_id'])

    if not channel:  # TODO
        bot.send_message('Ошибка, выбери канал из списка')
        return

    channel.save(as_current=True)

    ctx.state = 'Channels:sign'
    msg = bot.edit_message_text('Отправь новую подпись для постов в канале', kbs.EditSign())
    ctx.data['request_msg_id'] = msg.message_id


@on.message(state='Channels')
def _():
    bot.send_message('Ошибка, выбери канал из списка')


@on.button(kbs.EditSign.empty, state='Channels:sign')
def _(channel: models.Channel):
    helpers.update_post_sign(channel, text=None, entities=[])


@on.button(kbs.EditSign.cancel, state='Channels:sign')
def _():
    helpers.reset_ctx()
    bot.edit_message_text('Отменено')


@on.text(state='Channels:sign')
def _(channel: models.Channel):
    helpers.update_post_sign(channel, ctx.text, ctx.message.entities)
