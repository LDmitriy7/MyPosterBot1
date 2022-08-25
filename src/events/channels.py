from groof import events

from assets import commands, kbs

entry = events.command(commands.CHANNELS)
choice = events.button(kbs.Channels.channel, state='Channels')
any_message = events.message(state='Channels')
