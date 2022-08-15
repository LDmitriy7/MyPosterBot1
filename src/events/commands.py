from groof import on

from assets import commands, config

start = on.start(state='*')
start_by_admin = on.start(state='*', user_id=config.admins_ids)
cancel = on.command(commands.CANCEL, state='*')
test = on.command('test', state='*')
log = on.command(commands.LOGS, state='*', user_id=config.admins_ids)
