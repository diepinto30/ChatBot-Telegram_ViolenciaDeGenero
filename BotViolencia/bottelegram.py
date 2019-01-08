import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='🚨 Alerta de Violencia 🚨', callback_data='press')],
                   [InlineKeyboardButton(text='Ayuda continua 👋', callback_data='press2')],
               ])

    bot.sendMessage(chat_id, 'hola soy DiBot, ¿en qué te puedo ayudar?', reply_markup=keyboard)
    print(chat_id)


def report_aggression(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    if(query_data == 'press'):
        print('Callback Query:', query_id)
        bot.answerCallbackQuery(query_id, text='Usted a seleccionado la primera opción')
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Acto de violencia física 🥊👋', callback_data='pressA')],
                [InlineKeyboardButton(text='Acto de violencia psicológica o verbal 🧠🗣👋', callback_data='pressA2')],
            ])
        bot.sendMessage(648008717, '¿Qué tipo de acto de violencia quiere reportar?', reply_markup=keyboard)

    if(query_data == 'press2'):
        print('Callback Query:', query_id, query_data)
        bot.answerCallbackQuery(query_id, text='Got it 3')
        print('Callback Query:', query_id)
        bot.answerCallbackQuery(query_id, text='Usted a seleccionado la segunda opción')
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Acto de violencia física 🥊👋', callback_data='pressA')],
            [InlineKeyboardButton(text='Acto de violencia psicológica o verbal 🧠🗣👋', callback_data='pressA2')],
        ])
        bot.sendMessage(648008717, '¿Qué tipo de acto de violencia quiere reportar?', reply_markup=keyboard)


# def help_aggression(msg):
#     content_type, chat_type, chat_id = telepot.glance(msg)
#
#     keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text='Acto de violencia física 🥊👋', callback_data='pressA')],
#         [InlineKeyboardButton(text='Acto de violencia psicológica o verbal 🧠🗣👋', callback_data='pressA2')],
#     ])
#
#     bot.sendMessage(chat_id, '¿Qué tipo de acto de violencia quiere reportar?', reply_markup=keyboard)


TOKEN = '597926382:AAFG5pqIpVmtVRUPR2DhQLQosh0DBmE3nB4'  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': report_aggression}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(40)


