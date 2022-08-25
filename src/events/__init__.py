from groof import events

from assets import kbs
from . import channels, commands, edit_posts_sign, new_post, add_channel

text_cancel = events.text(kbs.Cancel.button, state='*')
any_query = events.callback_query(state='*')
