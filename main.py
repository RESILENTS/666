import telebot 
from telebot import types
import random
import time
import requests

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

    
@bot.message_handler(commands=['start'])
def handle_text (message):
    bot.send_message(message.chat.id, "Введите данные")
    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        txt = message.text
        bot.send_message(message.chat.id, "+" + txt)
    
    
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "🤖 BTC Banker":
        request = requests.get('https://github.com/' + txt)
        if request.status_code == 200:
            bot.send_message(message.chat.id, "+" + txt, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "-" + txt, parse_mode='Markdown')
            
    if message.text == "🤖 Chatex Bot":
        request = requests.get('https://github.com/b567567567567')
        if request.status_code == 200:
            bot.send_message(message.chat.id, "+", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "-", parse_mode='Markdown')
        
bot.polling(none_stop=True)
