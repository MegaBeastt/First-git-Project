import telebot
from telebot import types
import os
import random
from datetime import datetime
import traceback
import time
import sqlite3

TOKEN = '1863751456:AAG5Zui8pyQp_u9Et9WnYRkAJswb7mrtt4M'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id , 'Привет! Мы еще не знакомы :(')

bot.polling(none_stop=True)