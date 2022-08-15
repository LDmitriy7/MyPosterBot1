from groof import Dispatcher

import events
from . import channels, new_post, add_channel, logs, menu, test


def setup(dp: Dispatcher):
    dp.handle(events.commands.start_by_admin, menu.on_start_by_admin)
    dp.handle(events.commands.start, menu.on_start)

    dp.handle(events.commands.cancel, menu.cancel)
    dp.handle(events.text_cancel, menu.cancel)
    dp.handle(events.commands.test, test.run)

    dp.handle(events.channels.entry, channels.edit_posts_sign.ask_channel)
    dp.handle(events.channels.choice, channels.edit_posts_sign.ask_new)
    dp.handle(events.channels.any_message, channels.edit_posts_sign.ask_channel_from_list)

    dp.handle(events.edit_posts_sign.choice_empty, channels.edit_posts_sign.set_empty_post_sign)
    dp.handle(events.edit_posts_sign.cancel, channels.edit_posts_sign.cancel_editing_sign)
    dp.handle(events.edit_posts_sign.choice, channels.edit_posts_sign.set_new)

    dp.handle(events.new_post.photo, new_post.attach_photo)
    dp.handle(events.new_post.animation, new_post.attach_animation)
    dp.handle(events.new_post.choice_channel, new_post.save_channel)
    dp.handle(events.new_post.choice_publication_time_now, new_post.publish_post)
    dp.handle(events.new_post.choice_publication_time, new_post.schedule_post)

    dp.handle(events.add_channel.entry, add_channel.send_info)
    dp.handle(events.add_channel.bot_kicked, add_channel.delete)
    dp.handle(events.add_channel.bot_member_updated, add_channel.check_rights_and_add)

    dp.handle(events.commands.log, logs.send)
