import telebot 
from telebot import types
import random
import time
import username_check

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

username_check_a = ''

@bot.message_handler(commands=['start'])
def start(message):
    service = telebot.types.ReplyKeyboardMarkup(True)
    service.row('🔎 OSINT', '⚙️ Генераторы')
    service.row('🔀 Разные', 'ℹ️ FAQ')
    bot.send_message(message.from_user.id, 'Для начала нажмите необходимую кнопку', reply_markup=service)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == '🔎 OSINT':
        username_check = bot.send_message(message.from_user.id, 'Введите регистрационный номер:')
        bot.register_next_step_handler(username_check, get_car_model)

def get_car_model(message):
    global car_model
    car_model = message.text.upper()
    bot.send_message(message.from_user.id, '@username: ' + username_check_a')

bot.polling(none_stop=True)
