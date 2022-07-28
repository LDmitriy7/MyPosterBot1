from telebot import ctx, bot, on, exc, objects
from assets import commands, kbs, helpers, models


@on.command(commands.ADD_CHANNEL)
def _():
    bot.send_message('Отправь юзернейм канала', reply_markup=kbs.Cancel())
    ctx.state = 'AddChannel'


@on.text(state='AddChannel')
def _(channel: models.Channel):
    try:
        member = bot.get_chat_member(ctx.text)
    except exc.RequestError:
        bot.send_message('Канал не найден. Добавь меня в канал и попробуй снова')
        return

    if not isinstance(member, objects.ChatMemberOwner):
        bot.send_message('Вы должны быть владельцем канала')
        return

    chat = bot.get_chat(ctx.text)
    channel.chat_id = chat.id
    channel.title = chat.title
    channel.save_to_collection()

    helpers.reset_ctx()
    bot.send_message('Канал добавлен', kbs.remove)
