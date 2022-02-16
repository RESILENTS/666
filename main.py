import requests
import threading

from telebot import TeleBot
import telebot
import os

TOKEN = '5108669453:AAGuW4xE9QjnzHH27YRb_6xsZ5-NGuqpgjQ'

THREADS_LIMIT = 6666

chat_ids_file = 'chat_ids.txt'

block_list = 'block_list.txt'



keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
boom = types.KeyboardButton(text='🔥💣БОМБЕР')
titan = types.KeyboardButton(text='👅💦Титан-ГЕЛЬ')
stop = types.KeyboardButton(text='⛔️STOP')
info = types.KeyboardButton(text='ℹ️Информация')
stats = types.KeyboardButton(text='📈Статистика')
donat = types.KeyboardButton(text='💰Поддержать')
piar = types.KeyboardButton(text='💸 Реклама')
spons = types.KeyboardButton(text='🤝Наш партнер')

buttons_to_add = [boom, titan, stop, info, stats, donat, piar, spons]

keyboard.add(*buttons_to_add)





@bot.message_handler(commands=['start'])
def start(message):

    
        bot.send_message(message.chat.id, 'Добро пожаловать🙋‍♂!\nВыберите действие:', reply_markup=keyboard)

   
bot.polling(none_stop=True, interval=0)
