#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import telebot
import requests as req
# from geopy import geocoders
from decouple import config

token = config('token_bot')
# token_accu = environ['token_accu']
# token_yandex = environ['token_yandex']

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот, дарующий речь, приятно познакомитсья, {message.from_user.first_name}')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
