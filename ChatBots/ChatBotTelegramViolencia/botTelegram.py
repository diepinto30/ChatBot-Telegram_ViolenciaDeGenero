import telebot

bot = telebot.TeleBot("597926382:AAFG5pqIpVmtVRUPR2DhQLQosh0DBmE3nB4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


bot.polling()


from telebot import types
import telebot
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


TOKEN = '597926382:AAFG5pqIpVmtVRUPR2DhQLQosh0DBmE3nB4'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "hola soy DiBot, ¿en qué te puedo ayudar?")


markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('a')
itembtn2 = types.KeyboardButton('v')
itembtn3 = types.KeyboardButton('d')
markup.add(itembtn1, itembtn2, itembtn3)
bot.send_message(chat_id='@diepintoBot', text='Choose one letter:', reply_markup=markup)

bot.polling()

bot.get_me()
