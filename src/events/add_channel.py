from groof import events

from assets import commands

entry = events.command(commands.ADD_CHANNEL)
bot_kicked = events.my_chat_member(status=['left', 'kicked'], chat_type='channel', state='*')
bot_member_updated = events.my_chat_member(chat_type='channel', state='*')
