from dataclasses import dataclass


@dataclass
class Channel:
    username: str
    post_signs: list[str]
