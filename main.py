import telebot
from telebot import types
import time, os
import requests as r
from random import choice

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    service = telebot.types.ReplyKeyboardMarkup(True)
    service.row('🔎 OSINT', '⚙️ Генераторы')
    service.row('🔀 Разные', 'ℹ️ FAQ')
    bot.send_message(message.from_user.id, 'Для начала нажмите необходимую кнопку', reply_markup=service)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "⚙️ Генераторы":
        bot.send_message(message.chat.id, "/fake_address_generator ➖ Генератор фейковых данных", parse_mode='Markdown')
            
    if message.text == "🤖 Chatex Bot":
        request = requests.get('https://github.com/b567567567567')
        if request.status_code == 200:
            bot.send_message(message.chat.id, "+", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "-", parse_mode='Markdown')
            
bot.polling(none_stop=True)
