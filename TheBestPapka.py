import telebot
from telebot import types
import os
import random
from datetime import datetime
import traceback
import time
import sqlite3
import TheBestPapka1 as mc

TOKEN = '1863751456:AAG5Zui8pyQp_u9Et9WnYRkAJswb7mrtt4M'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id , 'Привет! Мы еще не знакомы :(')
    # user = mc.cheched_user(message)
    # print(user)
    # if user == (None, ) or user == ('Null',):
    #     bot.send_message(message.chat.id , 'Привет! Мы еще не знакомы :(')
    #     bot.send_message(message.chat.id , 'Как тебя зовут?')
    #     bot.register_next_step_handler(message , get_name)
    # else:
    #         bot.send_message(message.chat.id , 'Привет' + user[0] + ',Очень рад тебя видеть')
    #         bot.send_message(message.chat.id , 'Мои команды: \n/start\n/reg')
        

# def user_update(id,mode):
#         conn = sqlite3.connect('users_bot.db')
#         cursor = conn.cursor()
#         sql=''
       
#         if mode == 1:
#            sql = """UPDATE users SET name = '{1}', surname = '{2}',
#            age= {3} WHERE id = '{0}'""".format(id, name, surname, age)
#         elif mode == 2:
#             sql = """UPDATE users SET name ='Null', surname = 'Null',
#             age = Null WHERE id = '{0}'""".format(id)
#         cursor.execute(sql)
#         conn.commit()
#         conn.close()

# def get_name(message):  # получаем фамилию
#    global name
#    name = message.text
#    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
#    bot.register_next_step_handler(message, get_surname)

# def get_surname(message):
#    global surname
#    surname = message.text
#    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
#    bot.register_next_step_handler(message, get_age)


# def get_age(message):
#    global age
#    try:
#        age = int(message.text)  # проверяем, что возраст введен корректно
#        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
#        key_yes = types.InlineKeyboardButton(text='Да', callback_data='reg_yes')  # кнопка «Да»
#        key_no = types.InlineKeyboardButton(text='Нет', callback_data='reg_no')
#        keyboard.row(key_yes, key_no)
#        question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'
#        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#    except Exception:
#        bot.send_message(message.from_user.id, 'Введите возраст цифрами')
#        bot.send_message(message.from_user.id, 'Сколько тебе лет?')
#        bot.register_next_step_handler(message, get_age)

# @bot.callback_query_handler(func=lambda call: call.data.startswith('reg'))
# def callback_reg(call):
#     id = str(call.from_user.id)
#     if call.data == "reg_yes":
#         user_update(id, 1)
#         bot.send_message(call.message.chat.id, 'Изменения сохранены')
#     elif call.data == 'reg_no':
#         user_update(id, 2)
#         bot.send_message(call.message.chat.id, 'Данные удалены')

# @bot.message_handler(commands=['game'])
# def function(message):
#     print(message.text)
#     conn = sqlite3.connect(r"C:\Users\Amir\Desktop\example.db")
#     cursor = conn.cursor()
#     sql = "SELECT * FROM games"
#     cursor.execute(sql)
#     user = cursor.fetchall()
#     print(user)
#     for i in user:
#         bot.send_message(message.from_user.id, i[1])
#     conn.close()

# @bot.message_handler(commands=['admin'])
# def admin_message(message):
#     conn = sqlite3.connect('users_bot.db')
#     cursor = conn.cursor()
#     sql  = "SELECT * FROM users"
#     cursor.execute(sql)
#     users = cursor.fetchall()
#     str_user =''
#     for i in users:
#         str_user +=i[0] + ' ' + i[1] + ' ' + i[2] + ' ' + str([2]) + '\n'
#         bot.send_message(message.from_user.id, str_user)
#     # else:
#     #     bot.send_message(message.from_user.id, "Вам эта команда не доступна!" )


bot.polling(none_stop=True)