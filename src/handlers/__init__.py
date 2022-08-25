from groof import Handler

import events
from . import channels, new_post, add_channel, logs, menu, test

ALL = [
    Handler(events.commands.start_by_admin, menu.on_start_by_admin),
    Handler(events.commands.start, menu.on_start),
    Handler(events.commands.cancel, menu.cancel),
    Handler(events.commands.log, logs.send),
    Handler(events.commands.test, test.run),

    Handler(events.text_cancel, menu.cancel),

    Handler(events.channels.entry, channels.edit_posts_sign.ask_channel),
    Handler(events.channels.choice, channels.edit_posts_sign.ask_new),
    Handler(events.channels.any_message, channels.edit_posts_sign.ask_channel_from_list),

    Handler(events.edit_posts_sign.choice_empty, channels.edit_posts_sign.set_empty_post_sign),
    Handler(events.edit_posts_sign.cancel, channels.edit_posts_sign.cancel_editing_sign),
    Handler(events.edit_posts_sign.choice, channels.edit_posts_sign.set_new),

    Handler(events.new_post.photo, new_post.attach_photo),
    Handler(events.new_post.animation, new_post.attach_animation),
    Handler(events.new_post.choice_channel, new_post.save_channel),
    Handler(events.new_post.choice_publication_time_now, new_post.publish_post),
    Handler(events.new_post.choice_publication_time, new_post.schedule_post),

    Handler(events.add_channel.entry, add_channel.send_info),
    Handler(events.add_channel.bot_kicked, add_channel.delete),
    Handler(events.add_channel.bot_member_updated, add_channel.check_rights_and_add),
]
