from . import config
from telebot.objects import Keyboard


class Channels(Keyboard):
    all = [c.username for c in config.channels]

    def __init__(self):
        self.add_rows(*self.all)


class Signs(Keyboard):
    def __init__(self, channel: config.Channel):
        self.add_rows(*channel.post_signs)


class PublicationTime(Keyboard):
    now = 'Сейчас'

    def __init__(self):
        self.add_row(self.now)
