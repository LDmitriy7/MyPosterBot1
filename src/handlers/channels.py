from telebot import on, bot, ctx

from assets import commands, kbs, helpers, models


@on.command(commands.CHANNELS)
def _():
    ctx.state = 'Channels'
    msg = bot.send_message('Выбери канал для редактирования', reply_markup=kbs.Channels())
    ctx.data['request_msg_id'] = msg.message_id


@on.text(state='Channels')
def _():
    channel = models.Channel.find(title=ctx.text)

    if not channel:
        bot.send_message('Ошибка, выбери канал из списка')
        return

    channel.save(as_current=True)

    ctx.state = 'Channels:sign'
    bot.delete_message(ctx.data['request_msg_id'])
    msg = bot.send_message('Отправь новую подпись для постов в канале', kbs.EditSign())
    ctx.data['request_msg_id'] = msg.message_id


@on.button(kbs.EditSign.empty, state='Channels:sign')
def _(channel: models.Channel):
    helpers.update_post_sign(channel, text=None, entities=[])


@on.text(state='Channels:sign')
def _(channel: models.Channel):
    helpers.update_post_sign(channel, ctx.text, ctx.message.entities)
