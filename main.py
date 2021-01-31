import telebot 
from telebot import types
import random
import time
import requests
import constant

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

    
@bot.message_handler(commands=['start'])
def another_process(message):
    bot.send_message(message.chat.id, 'Ссылка на товар ' + message.text)

@bot.message_handler(commands=['add'])
def handle_start(message):
    message = bot.send_message(message.chat.id, "Введите ссылку на товар", disable_notification=True)
    url = message.text
    constants.items.append(url)
    bot.register_next_step_handler(message, another_process)
    bot.send_message(message.chat.id, 'Ссылка на товар ' + url)
    
    
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "🤖 BTC Banker":
        request = requests.get('https://github.com/')
        if request.status_code == 200:
            bot.send_message(message.chat.id, "+", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "-", parse_mode='Markdown')
            
    if message.text == "🤖 Chatex Bot":
        request = requests.get('https://github.com/b567567567567')
        if request.status_code == 200:
            bot.send_message(message.chat.id, "+", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "-", parse_mode='Markdown')
        
bot.polling(none_stop=True)
