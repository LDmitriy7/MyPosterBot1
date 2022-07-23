class Scene:
    @classmethod
    def enter(cls): ...

    @classmethod
    def next(cls): ...


class NewPost(Scene):
    channel = 'NewPost:channel'
    sign = 'NewPost:sign'
