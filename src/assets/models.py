from dataclasses import dataclass, field

from telebot import UserProxyModel, objects


@dataclass
class Channel(UserProxyModel):
    chat_id: str = None
    title: str = None
    post_sign: str = None
    post_sign_entities: list[objects.MessageEntity] = field(default_factory=list)


@dataclass
class Post(UserProxyModel):
    photos: list[str] = field(default_factory=list)
