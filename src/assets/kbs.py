from groof.objects import Keyboard, ReplyKeyboardRemove, InlineKeyboard, CallbackButton

from . import models


class Channels(InlineKeyboard):
    channel = CallbackButton(text='{title}', id='Channels:channel')

    def __init__(self):
        for c in models.Channel.find_all():
            self.add_row(
                self.channel(title=c.title, chat_id=c.chat_id)
            )


class Cancel(Keyboard):
    button = 'Отменить'

    def __init__(self):
        self.add_row(self.button)


remove = ReplyKeyboardRemove()


class EditSign(InlineKeyboard):
    empty = CallbackButton('Без подписи')
    cancel = CallbackButton('Отменить')

    def __init__(self):
        self.add_row(self.empty, self.cancel)


class PublicationTime(InlineKeyboard):
    now = CallbackButton('Сейчас')

    def __init__(self):
        self.add_row(self.now)
