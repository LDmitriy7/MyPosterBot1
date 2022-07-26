import time
from threading import Lock

from telebot import on, bot, ctx

from assets import models, helpers

lock = Lock()
FIRST_MEDIA_IN_GROUP = True


@on.command('test', state='*')
def _():
    ctx.state = 'test'
    bot.send_message('Отправь мне пост')


@on.photo(state='test')
def _():
    global FIRST_MEDIA_IN_GROUP

    lock.acquire()

    if FIRST_MEDIA_IN_GROUP:
        models.Post(channel=str(ctx.user_id), sign='test', photos=[ctx.file_id]).save()

        FIRST_MEDIA_IN_GROUP = False
        lock.release()
        time.sleep(1)
        FIRST_MEDIA_IN_GROUP = True

        helpers.publish_post()
        ctx.state = 'test'
    else:
        post = models.Post.get()
        post.photos.append(ctx.file_id)
        post.save()
        lock.release()


@on.photo(state='test:media_group')
def _(post: models.Post):
    post.photos.append(ctx.file_id)
