from groof import bot, objects


def send():
    bot.send_document(objects.InputFile('.log', 'logs.txt'))
