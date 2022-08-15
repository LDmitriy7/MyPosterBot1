from groof import on

from assets import commands

entry = on.command(commands.ADD_CHANNEL)
bot_kicked = on.my_chat_member(status=['left', 'kicked'], chat_type='channel', state='*')
bot_member_updated = on.my_chat_member(chat_type='channel', state='*')
