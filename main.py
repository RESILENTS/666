import telebot 
from telebot import types
import random
import time
import requests

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

    
@bot.message_handler(commands=['start'])
def another_process(message):
    bot.send_message(message.chat.id, 'Ссылка на товар ' + message.text)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if message.text == "✅Проверить оплату":
       msg = bot.send_message(call.message.chat.id, 'Введите текст')
       bot.register_next_step_handler(msg, q_2)

def q_2(message):
    print(message.text)
    
    
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
