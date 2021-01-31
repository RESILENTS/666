import telebot 
from telebot import types
import random
import time
import requests

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)
    
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.from_user.id, '*🤖 BTCVoucherGen 2.0:* Генератор BTC чеков. Скрипт генерирует ссылки для обнала BTC чеков в *Telegram* ботах.\n\n', parse_mode='Markdown')
    
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "🤖 BTC Banker":
        request = requests.get('https://vk.com/durov')
        if request.status_code == 200:
            bot.send_message(message.chat.id, "+", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "-", parse_mode='Markdown')
        
bot.polling(none_stop=True)
