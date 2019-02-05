#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

    bot.sendMessage(chat_id, 'Hola soy Dibot un asistente virtual, ¿En qué te puedo ayudar?', reply_markup=keyboard)
    print(chat_id)
    global idc
    idc = chat_id
    global text
    text = content_type


def report_aggression(msg):  # def de reportes de violencia
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    if query_data == 'press':
        bot.answerCallbackQuery(query_id, text='Usted a seleccionado la primera opción')
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Acto de violencia física 🥊👋', callback_data='pressA')],
                [InlineKeyboardButton(text='Acto de violencia psicológica o verbal 🧠🗣👋', callback_data='pressA2')],
            ])
        bot.sendMessage(idc, '_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
        bot.sendMessage(idc, '¿Qué tipo de acto de violencia quiere reportar?', reply_markup=keyboard)

    if query_data == 'press2':
        bot.answerCallbackQuery(query_id, text='Usted a seleccionado la segunda opción')
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='¿Qué hago cuando \npuedo ser agredida/o?', callback_data='pressV')],
            [InlineKeyboardButton(text='tengo que poner algo aqui pero nose', callback_data='pressV2')],
        ])
        bot.sendMessage(idc, '¿qqqqqqQué tipo de acto de violencia quiere reportar?', reply_markup=keyboard)

    # Fisica
    if query_data == 'pressA':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Si.', callback_data='pressRVF')],
            [InlineKeyboardButton(text='No.', callback_data='pressRVFNO')],
        ])
        bot.sendMessage(idc, 'Denunciar ahora el acto de violencia Física ...', reply_markup=keyboard)


    if query_data == 'pressRVF':
        bot.sendMessage(idc, 'Su denuncia esta siendo procesada. Gracias por confiar en nosotros, DiBot estaré siempre cuando nos necesites.')
        bot.sendMessage(idc, '_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='🚨 Alerta de Violencia 🚨', callback_data='press')],
            [InlineKeyboardButton(text='Ayuda continua 👋', callback_data='press2')],
        ])

        bot.sendMessage(idc, 'Hola soy Dibot un asistente virtual, ¿En qué te puedo ayudar?', reply_markup=keyboard)


    if query_data == 'pressRVFNO':
        bot.sendMessage(idc, 'Desea contactar con algún profesional para poder solucionar o que ahora le esta sucediendo.', reply_markup=keyboard)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Me seria de mucha ayuda.', callback_data='pressme')],
            [InlineKeyboardButton(text='En otro momento.', callback_data='pressrg1')],
        ])

    if query_data == 'pressme':
        bot.sendMessage(idc, 'Desea contactar con algún profesional para poder solucionar o que ahora le esta sucediendo.', reply_markup=keyboard)
        bot.sendMessage(idc, '_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Link', callback_data='press333')],
            [InlineKeyboardButton(text='Regresar', callback_data='pressrg1')],
        ])

    if query_data == 'pressrg1':
        bot.sendMessage(idc, '_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='🚨 Alerta de Violencia 🚨', callback_data='press')],
            [InlineKeyboardButton(text='Ayuda continua 👋', callback_data='press2')],
        ])

        bot.sendMessage(idc, 'Hola soy Dibot un asistente virtual, ¿En qué te puedo ayudar?', reply_markup=keyboard)


    # Psicologica
    if query_data == 'pressA2':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Si.', callback_data='pressRVF2')],
            [InlineKeyboardButton(text='No.', callback_data='pressRVFNO2')],
        ])
        bot.sendMessage(idc, 'Denunciar ahora el acto de violencia Psicologica o verbal ...', reply_markup=keyboard)


    if query_data == 'pressRVF2':
        bot.sendMessage(idc, 'Su denuncia esta siendo procesada. Gracias por confiar en nosotros, DiBot estaré siempre cuando nos necesites.')
        bot.sendMessage(idc, '_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='🚨 Alerta de Violencia 🚨', callback_data='press')],
            [InlineKeyboardButton(text='Ayuda continua 👋', callback_data='press2')],
        ])

        bot.sendMessage(idc, 'Hola soy Dibot un asistente virtual, ¿En qué te puedo ayudar?', reply_markup=keyboard)


    if query_data == 'pressRVFNO':
        bot.sendMessage(idc, 'Desea contactar con algún profesional para poder solucionar o que ahora le esta sucediendo.', reply_markup=keyboard)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Me seria de mucha ayuda.', callback_data='pressme')],
            [InlineKeyboardButton(text='En otro momento.', callback_data='pressrg1')],
        ])


TOKEN = ''  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message, 'callback_query': report_aggression}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
