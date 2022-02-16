import requests
import threading

from telebot import TeleBot
import telebot
import os

TOKEN = '5108669453:AAGuW4xE9QjnzHH27YRb_6xsZ5-NGuqpgjQ'

THREADS_LIMIT = 6666

chat_ids_file = 'chat_ids.txt'

block_list = 'block_list.txt'


@bot.message_handler(commands=['start'])
def start(message):

    
        bot.send_message(message.chat.id, 'Добро пожаловать🙋‍♂!\nВыберите действие:', reply_markup=keyboard)

   
bot.polling(none_stop=True, interval=0)
