from dataclasses import dataclass, field

from telebot import UserProxyModel


@dataclass
class Channel:
    username: str
    post_signs: list[str]


@dataclass
class Post(UserProxyModel):
    channel: str = None
    sign: str = None
    photos: list[str] = field(default_factory=list)
