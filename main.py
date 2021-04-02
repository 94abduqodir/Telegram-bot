import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = '1714797807:AAHSiVw9XGX6fX3OwRtlaamVdMRZMg7BvHI'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):

    username = message.from_user.first_name
    msg = f'Assalomu alaykum {username}, bu bot ixtiyoriy matinni KIRLDAN - LOTINGA && ' \
               'LOTINDAN - KIRLGA o\'tkazib beradi!'
    msg +='\nMatn kiriting:'

    bot.reply_to(message, msg)


@bot.message_handler(func=lambda message: True)
def echo_all(message):

    def translite(message):
        msg = message.text

        if msg.isascii():
            return to_cyrillic(msg)
        else:
            return to_latin(msg)

    bot.reply_to(message, translite(message))




bot.polling()

