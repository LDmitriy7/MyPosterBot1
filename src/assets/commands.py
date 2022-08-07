from telebot import objects, bot, ctx

START = 'start'
TEST = 'test'
ADD_CHANNEL = 'add_channel'
CHANNELS = 'channels'
CANCEL = 'cancel'
LOGS = 'logs'

USER_COMMANDS = [
    objects.BotCommand(START, 'Перезапуск'),
    objects.BotCommand(ADD_CHANNEL, 'Добавить канал'),
    objects.BotCommand(CHANNELS, 'Настройки каналов'),
    objects.BotCommand(CANCEL, 'Отменить'),
    objects.BotCommand(TEST, 'Тест'),
    objects.BotCommand(LOGS, 'Логи'),
]


def setup():
    bot.delete_my_commands(scope=objects.BotCommandScopeChat(ctx.user_id))
    bot.set_my_commands(USER_COMMANDS)
