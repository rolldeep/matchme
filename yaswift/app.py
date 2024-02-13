import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def handle_text(update, context):
    text = update.message.text
    response = requests.post("http://localhost:5000/create_transfer", json={"text": text})
    update.message.reply_text(response.text)

def main():
    TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()