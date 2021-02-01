import telebot 
from telebot import types
import random
import time
import string

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def selfmyself(message):
    service = telebot.types.ReplyKeyboardMarkup(True)
    service.row('🤖 Chatex Bot', '🤖 BTC Banker')
    
    message = bot.send_message(message.chat.id, "Введите ссылку на товар", disable_notification=True, reply_markup=service)
    url = message.text
    constants.items.append(url)
    bot.register_next_step_handler(message, another_process)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "🤖 BTC Banker":
        new_pas = "https://t.me/BTC_CHANGE_BOT?start=с_"
        bot.send_message(message.chat.id, new_pas, disable_web_page_preview=True)
        
    if message.text == "🤖 Chatex Bot":
        new_pas = "https://t.me/Chatex_bot?start=c_"
        bot.send_message(message.chat.id, new_pas, disable_web_page_preview=True)

bot.polling(none_stop=True)
