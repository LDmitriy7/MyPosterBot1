from groof import on

from assets import kbs

choice_empty = on.button(kbs.EditSign.empty, state='Channels:sign')
cancel = on.button(kbs.EditSign.cancel, state='Channels:sign')
choice = on.text(state='Channels:sign')
