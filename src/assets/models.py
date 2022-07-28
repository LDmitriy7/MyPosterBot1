from dataclasses import dataclass, field

from telebot import UserProxyModel


@dataclass
class Channel(UserProxyModel):
    chat_id: str = None
    title: str = None
    post_sign: str = None


@dataclass
class Post(UserProxyModel):
    photos: list[str] = field(default_factory=list)
