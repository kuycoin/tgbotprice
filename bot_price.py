import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import requests

telegram_bot_token = "KuyRaiAiSUS"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher
preprice = ""
def get_prices():
   
    crypto_data = requests.get("https://008vruj3t7.execute-api.ap-northeast-1.amazonaws.com/dev/getKuyPrice")
    data = crypto_data.text
    if data == "nan" or data == "NaN":
        crypto_data = requests.get("https://008vruj3t7.execute-api.ap-northeast-1.amazonaws.com/dev/getKuyPrice")
        data = crypto_data.text
    return data

def start(update, context):
    curprice = get_prices()
   
    chat_id = update.effective_chat.id
    message = f"KuyCOIN \nPrice: {str(curprice[0:8])}฿"

    context.bot.send_message(chat_id=chat_id, text=message)

def setprice(update, context):
    curprice = get_prices()
    chat_id = update.effective_chat.id
    message = f"KuyCOIN \nPrice: {str(context.args[0:8])}฿"

    context.bot.send_message(chat_id=chat_id, text=message)
# def start_callback(update, context):
#     user_says = " ".join(context.args)
#     update.message.reply_text("You said: " + user_says)

# ...

# dispatcher.add_handler(CommandHandler("start", start_callback))

dispatcher.add_handler(CommandHandler("kuyprice", start))
dispatcher.add_handler(CommandHandler("setprice", setprice , pass_args=True))
updater.start_polling()
# import requests


# def get_prices():
   
#     crypto_data = requests.get(
#         "http://localhost:3000/dev/getKuyPrice")

#     data = crypto_data.text
#     return data


# if __name__ == "__main__":
#     print(get_prices())
# import telegram
# from telegram.ext import Updater
# from telegram.ext import CommandHandler

# telegram_bot_token = ""

# updater = Updater(token=telegram_bot_token, use_context=True)
# dispatcher = updater.dispatcher


# def start(update, context):
#     chat_id = update.effective_chat.id
#     context.bot.send_message(chat_id=chat_id, text="Hello World")


# dispatcher.add_handler(CommandHandler("start", start))
# updater.start_polling()
