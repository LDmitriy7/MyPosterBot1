from telebot.objects import Keyboard, ReplyKeyboardRemove

from . import models


class Channels(Keyboard):

    def __init__(self):
        channels = models.Channel.get_collection()
        self.add_rows(*[c.title for c in channels])


class PublicationTime(Keyboard):
    now = 'Сейчас'

    def __init__(self):
        self.add_row(self.now)


class Cancel(Keyboard):
    button = 'Отменить'

    def __init__(self):
        self.add_row(self.button)


remove = ReplyKeyboardRemove()
