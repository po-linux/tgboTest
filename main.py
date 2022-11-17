#!/usr/bin/env python3

# My first telegram bot
# https://t.me/polina_first_bot


import telebot
from random import randrange
from telebot.types import ReplyKeyboardMarkup as keyboard


token_file = open('/Users/polina/Documents/.my_first_botoken')
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


@bot.message_handler(content_types=['text'])
def mess(message):
    print(message.from_user.first_name, "Sended", message.text)
    input_message = message.text.strip().lower()
    if input_message == 'flip':
        rand = randrange(2)
        msg = "Yes" if rand else "No"

        bot.send_message(
            message.chat.id,
            msg,
            parse_mode='html',
            reply_markup=board
        )


bot.polling(none_stop=True)
