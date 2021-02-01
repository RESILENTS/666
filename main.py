import telebot 
from telebot import types
import time
 
token = "1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    message = bot.send_message(message.chat.id, "Введите ссылку на товар", disable_notification=True)
    url = message.text
    constants.items.append(url)
    bot.register_next_step_handler(message, another_process)
    
@bot.message_handler(commands=['add'])
def another_process(message):
    bot.send_message(message.chat.id, 'Ссылка на товар ' + message.text)
