from groof import on

from assets import kbs
from . import channels, commands, edit_posts_sign, new_post

text_cancel = on.text(kbs.Cancel.button, state='*')
