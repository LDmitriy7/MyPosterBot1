from dataclasses import dataclass, field

from telebot import Session


@dataclass
class NewPost(Session):
    photos: list = field(default_factory=list)
    channel: str = None
    sign: str = None
