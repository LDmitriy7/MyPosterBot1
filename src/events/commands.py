from groof import events

from assets import commands, config

start = events.start(state='*')
start_by_admin = events.start(state='*', user_id=config.admins_ids)
cancel = events.command(commands.CANCEL, state='*')
test = events.command('test', state='*')
log = events.command(commands.LOGS, state='*', user_id=config.admins_ids)
