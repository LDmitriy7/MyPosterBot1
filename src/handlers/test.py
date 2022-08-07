from telebot import on, ctx

from assets import kbs


@on.button(kbs.Channels.channel, state='*')
def _():
    print(ctx.button['chat_id'])
