import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


def on_chat_message(msg):  # accion de comienzo
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='🚨 Alerta de Violencia 🚨', callback_data='press')],
                   [InlineKeyboardButton(text='Ayuda continua 👋', callback_data='press2')],
               ])

    bot.sendMessage(chat_id, 'hola soy DiBot, ¿en qué te puedo ayudar?', reply_markup=keyboard)
    print(chat_id)


def report_aggression(msg):  # def de reportes de violencia
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    if query_data == 'press':
        bot.answerCallbackQuery(query_id, text='Usted a seleccionado la primera opción')
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Acto de violencia física 🥊👋', callback_data='pressA')],
                [InlineKeyboardButton(text='Acto de violencia psicológica o verbal 🧠🗣👋', callback_data='pressA2')],
            ])
        bot.sendMessage(648008717, '_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
        bot.sendMessage(648008717, '¿Qué tipo de acto de violencia quiere reportar?', reply_markup=keyboard)

    if query_data == 'press2':
        bot.answerCallbackQuery(query_id, text='Usted a seleccionado la segunda opción')
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='¿Qué hago cuando \npuedo ser agredida/o?', callback_data='pressV')],
            [InlineKeyboardButton(text='tengo que poner algo aqui pero nose', callback_data='pressV2')],
        ])
        bot.sendMessage(648008717, '¿Qué tipo de acto de violencia quiere reportar?', reply_markup=keyboard)

    if query_data == 'pressV':
        print(query_data)
        print("dentro del pressV")
        bot.sendMessage(648008717, 'vamos bien estoy aquí || pressV')
    else:
        if query_data == 'pressV2':
            print(query_data)
            print("dentro del pressV2")
            bot.sendMessage(648008717, 'vamos bien estoy aquí || pressV2')

    # def help_aggression():
    #     query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query2')
    #     print('Callback Query:', query_id, from_id, query_data)

        # keyboard = InlineKeyboardMarkup(inline_keyboard=[
        #     [InlineKeyboardButton(text='Acto de violencia ', callback_data='pressA')],
        #     [InlineKeyboardButton(text='Acto de violencia sss', callback_data='pressA2')],
        # ])
        # bot.sendMessage(chat_id, '¿Qué tipo de acto de violencia quiere reportar?', reply_markup=keyboard)


TOKEN = '597926382:AAFG5pqIpVmtVRUPR2DhQLQosh0DBmE3nB4'  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message, 'callback_query': report_aggression, 'callback_query2': report_aggression}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(40)


