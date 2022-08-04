from telebot.objects import Keyboard, ReplyKeyboardRemove, InlineKeyboard, CallbackButton

from . import models


class Channels(Keyboard):

    def __init__(self):
        channels = models.Channel.find_all()
        self.add_rows(*[c.title for c in channels])


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


class PublicationTime(Keyboard):
    now = 'Сейчас'

    def __init__(self):
        self.add_row(self.now)
