from dataclasses import dataclass, field

from telebot import UserModel, UserProxyModel


@dataclass
class Channel(UserModel):
    chat_id: int = None
    title: str = None
    post_sign: str = None


@dataclass
class Post(UserProxyModel):
    photos: list[str] = field(default_factory=list)
    gif: str = None
    caption: str = None
