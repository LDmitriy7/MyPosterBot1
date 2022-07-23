from telebot import on, ctx, bot

from assets import kbs, helpers


@on.photo(state='NewPost')
def _():
    ctx.data['photos'] = ctx.data['photos'] + [ctx.file_id]


@on.text(kbs.Channels.all, state='NewPost')
def _():
    ctx.data['channel'] = ctx.text
    channel = helpers.find_channel(ctx.text)

    match len(channel.post_signs):
        case 0:
            helpers.publish_post()
        case 1:
            ctx.data['sign'] = channel.post_signs[0]
            helpers.publish_post()
        case _:
            bot.send_message('Выбери подпись:', kbs.Signs(channel))
            ctx.state = 'NewPost:sign'


@on.text(state='NewPost:sign')
def _():
    ctx.data['sign'] = ctx.text
    helpers.publish_post()
