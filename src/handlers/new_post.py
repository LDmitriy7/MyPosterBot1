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
            helpers.ask_publication_time()
        case 1:
            ctx.data['sign'] = channel.post_signs[0]
            helpers.ask_publication_time()
        case _:
            bot.send_message('Выбери подпись:', kbs.Signs(channel))
            ctx.state = 'NewPost:sign'


@on.text(state='NewPost:sign')
def _():
    ctx.data['sign'] = ctx.text
    helpers.ask_publication_time()


@on.text(kbs.PublicationTime.now, state='NewPost:publication_time')
def _():
    helpers.publish_post()


@on.text(state='NewPost:publication_time')
def _():
    try:
        publication_time = helpers.parse_datetime(ctx.text)
    except ValueError:
        bot.send_message('Неправильный формат времени')
        return

    helpers.publish_post(publication_time)
