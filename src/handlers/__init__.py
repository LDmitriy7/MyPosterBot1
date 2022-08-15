from groof import handle

import events
from . import channels
from .main import on_start, on_start_by_admin, cancel
from .test import on_test


def setup():
    handle(events.commands.start_by_admin, on_start_by_admin)
    handle(events.commands.start, on_start)

    handle(events.commands.cancel, cancel)
    handle(events.button_cancel, cancel)
    handle(events.commands.test, on_test)

    handle(events.channels.entry, channels.edit_posts_sign.ask_channel)
    handle(events.channels.choice, channels.edit_posts_sign.ask_new)
    handle(events.channels.any_message, channels.edit_posts_sign.ask_channel_from_list)

    handle(events.edit_posts_sign.choice_empty, channels.edit_posts_sign.set_empty_post_sign)
    handle(events.edit_posts_sign.cancel, channels.edit_posts_sign.cancel_editing_sign)
    handle(events.edit_posts_sign.choice, channels.edit_posts_sign.set_new)

    # from . import add_channel
    # from . import new_post
    # from . import admin
