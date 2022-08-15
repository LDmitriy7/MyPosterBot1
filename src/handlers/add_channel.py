import helpers
from assets import commands, texts, models
from groof import ctx, bot, on, objects, html


@on.command(commands.ADD_CHANNEL)
def _():
    bot.send_message(texts.adding_channel_info)


@on.my_chat_member(status=['left', 'kicked'], chat_type='channel', state='*')
def _():
    if channel := models.Channel.find(chat_id=ctx.chat_id):
        channel.delete()

    title = html.a(ctx.chat.title, helpers.get_url(ctx.chat))
    bot.send_message(f'Канал {title} отключен', chat_id=ctx.user_id)


@on.my_chat_member(chat_type='channel', state='*')
def _():
    chat_member = ctx.new_chat_member

    if not isinstance(chat_member, objects.ChatMemberAdministrator):
        return

    if models.Channel.find(chat_id=ctx.chat_id):
        return

    title = html.a(ctx.chat.title, helpers.get_url(ctx.chat))

    if not chat_member.can_post_messages:
        text = texts.ask_posting_right.format(title=title)
        bot.send_message(text, chat_id=ctx.user_id)
        return

    channel = models.Channel()
    channel.chat_id = ctx.chat_id
    channel.title = ctx.chat.title
    channel.save()

    helpers.reset_ctx()
    bot.send_message(f'Канал {title} успешно подключен', chat_id=ctx.user_id)

    if helpers.has_one_channel():
        bot.send_message('Теперь ты можешь отправлять или пересылать мне посты в любое время', chat_id=ctx.user_id)
