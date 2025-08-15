from telegram.updater import Updater
from telegram.handlers import MessageHandler
from telegram.types import Update
from config import token


def handle_message(update: Update):
    message = update.message


    if message.text:
        if message.text == '/start':
            message.reply_text(token, 'Assalomu aleykum. ECHO BOT')
        else:
            message.reply_text(token, message.text)

    elif message.contact:
        pass
    elif message.photo:
        pass
    elif message.sticker:
        pass                



updater = Updater(token)
dispatcher = updater.dispatcher


dispatcher.add_handlers(MessageHandler(handle_message))

updater.start_polling()        