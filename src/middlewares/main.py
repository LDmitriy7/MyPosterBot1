from telebot import on, ctx, exc


@on.message(state='*')
def check_access():
    if ctx.user_id not in [724477101]:
        raise exc.StopProcessing()


check_access.exclusive = False
check_access.check_first = True
