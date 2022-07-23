from dataclasses import dataclass, field


@dataclass
class Channel:
    username: str
    post_signs: list[str]

    def find(self, username):
        pass


@dataclass
class NewPost:
    photos: list = field(default_factory=list)
    channel: str = None
    sign: str = None
