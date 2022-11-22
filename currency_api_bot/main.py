#!/usr/bin/env python3

# My currency telegram bot
# t.me/currency_polina_bot


import telebot
from random import randrange
from telebot.types import ReplyKeyboardMarkup as keyboard

import currency_api as ca

token_file = open('/Users/polina/Documents/.currency_api_botoken')
token = token_file.read().rstrip('\n')
bot = telebot.TeleBot(token)

board = keyboard(True, True)
board.row('Flip')


@bot.message_handler(commands=['start'])
def start(message):
    print(message.from_user.first_name, "Connected")
    greeting = f"<b>Hello, {message.from_user.first_name}!</b>\nLet's play!"
    bot.send_message(
        message.chat.id,
        greeting,
        parse_mode='html',
        reply_markup=board
    )


@bot.message_handler(commands=['help'])     #функция, для обработки команды /help
def help(message):
    print(message.from_user.first_name, "Connected")
    help_mes = ca.get_help()
    bot.send_message(
        message.chat.id,
        help_mes,
        parse_mode='html',
        reply_markup=board
    )


@bot.message_handler(content_types=['text'])        #функция, для обработки полученных сообщений текстом
def mess(message):
    print(message.from_user.first_name, "Sended", message.text)
    input_message = message.text.strip().upper()
    if input_message == 'HELP':
        help_mes = ca.get_help()

        bot.send_message(
            message.chat.id,
            help_mes,
            parse_mode='html',
            reply_markup=board
        )



bot.polling(none_stop=True)
