from groof import on

from assets import commands, kbs

entry = on.command(commands.CHANNELS)
choice = on.button(kbs.Channels.channel, state='Channels')
any_message = on.message(state='Channels')
