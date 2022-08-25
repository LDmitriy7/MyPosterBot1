from groof import events

from assets import kbs

choice_empty = events.button(kbs.EditSign.empty, state='Channels:sign')
cancel = events.button(kbs.EditSign.cancel, state='Channels:sign')
choice = events.text(state='Channels:sign')
