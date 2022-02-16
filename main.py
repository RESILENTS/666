import telebot
from telebot import types
import time, os
import requests as r
from random import choice

bot.remove_webhook()

token = '5108669453:AAGuW4xE9QjnzHH27YRb_6xsZ5-NGuqpgjQ'
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
        bot.send_message(message.chat.id, "/fake_data_generator Генератор фейковых данных.\n/giftcardgenerator Генератор Gift кодов.", parse_mode='Markdown')
            
    if message.text == "🤖 Chatex Bot":
        request = requests.get('https://github.com/b567567567567')
        if request.status_code == 200:
            bot.send_message(message.chat.id, "+", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "-", parse_mode='Markdown')
            
bot.polling(none_stop=True)
