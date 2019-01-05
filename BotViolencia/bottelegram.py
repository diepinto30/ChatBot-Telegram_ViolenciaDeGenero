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


# markup = types.ReplyKeyboardMarkup(row_width=2)
# itembtn1 = types.KeyboardButton('a')
# itembtn2 = types.KeyboardButton('v')
# itembtn3 = types.KeyboardButton('d')
# markup.add(itembtn1, itembtn2, itembtn3)
# bot.send_message(chat_id="@diepintoBot", text='Choose one letter:', reply_markup=markup)
print("vale....")
bot.polling()

bot.get_me()





'''
from telebot.apihelper import edit_message_reply_markup
import telebot
from telebot import ReplyKeyboarMarkup
from telebot.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler)
import logging

logging.basicConfig(format='%(asctime)s - %(names)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, PYPING_CHOICE = range(3)

reply_keybord = [['Reportar Violencia', 'Centro de ayuda']]

markup = ReplyKeyboarMarkup(reply_keybord, one_time_keyboard=True)


def facts_to_str(user_data):
    facts = list()

    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])


def start(bot, update):
    update.message.reply_text('hola mi nombre es DiBot, ¿en qué te puedo ayudar?', reply_markup=markup)

    return CHOOSING


def regular_choice(bot, update, user_data):
    text = update.message.text
    user_data['choice'] = text
    update.message.reply_text('tu {}? Si, me encanta')

    return TYPING_REPLY


def received_information(bot, update, user_data):
    text = update.message.text
    category = user_data['choide']
    user_data[category] = text
    del user_data['choide']

    update.message.reply_text('lo que me ha dicho hasta ahora', '{}', 'puede añadir mas infformación'.format(facts_to_str(user_data)), reply_markup=markup)

    return CHOOSING


def done(bot, update, user_data):
    if 'choide' in user_data:
        del  user_data['choide']

    update.message.reply_text('Todo esto se de usted', '{}', "puedes decirnos más".format(facts_to_str(user_data)), reply_markup=markup)

    user_data.clear()
    return ConversationHandler.END


def error(bot, update, error):
    logger.warning('la actualización "%s" provocó el error "%s"', update, error)


def main():
    updater = Updater('597926382:AAFG5pqIpVmtVRUPR2DhQLQosh0DBmE3nB4')
    dp = updater.dispatcher

    conv_handler = ConversationHandler(entry_points=[ConversationHandler('start', start)],
                                       states={
                                           CHOOSING: [RegexHandler('^(Reportar Violencia|Centro de ayuda)$', regular_choice(), pass_user_data=True),],
                                           TYPING_REPLY: [MessageHandler(Filters.text, received_information(), pass_user_data=True),],
                                       },
                                       fallbacks=[RegexHandler('^Done$', done(), pass_user_data=True)]
                                       )
    dp.add_handler(conv_handler)
    dp.add_error_handler(error)
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
'''
