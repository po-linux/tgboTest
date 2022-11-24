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
board.row('Date')

@bot.message_handler(commands=['start'])
def start(message):
    print(message.from_user.first_name, "Connected")
    greeting = f"<b>Привет, {message.from_user.first_name}!</b>\nКурс валют обновлён!"
    bot.send_message(
        message.chat.id,
        greeting,
        parse_mode='html',
        reply_markup=board
    )

    
@bot.message_handler(commands=['help'])
def help(message):
    help_msg = ca.get_help()
    bot.send_message(
        message.chat.id,
        help_msg,
        parse_mode='html',
        reply_markup=board
    )


@bot.message_handler(commands=['date'])
def date(message):
    date_msg = ca.get_date()
    bot.send_message(
        message.chat.id,
        date_msg,
        parse_mode='html',
        reply_markup=board
    )


@bot.message_handler(content_types=['text'])
def mess(message):
    print(message.from_user.first_name, "Sended", message.text)
    input_msg = message.text.strip().upper()

    if input_msg == 'HELP':
        return help(message)

    if input_msg == 'DATE':
        return date(message)

    output_msg = ca.get_currency_rate(input_msg)    

    bot.send_message(
        message.chat.id,
        output_msg,
        parse_mode='html',
        reply_markup=board
    )


bot.polling(none_stop=True)
