import telebot 
from telebot import types
import random
import time

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

markup_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
btn_new = telebot.types.KeyboardButton('Запись нового авто')
btn_verify = telebot.types.KeyboardButton('Проверка авто')
markup_menu.add(btn_new, btn_verify)

car_plate = ''

@bot.message_handler(commands=['start'])
def start(message):
    service = telebot.types.ReplyKeyboardMarkup(True)
    service.row('🔎 OSINT', '⚙️ Генераторы')
    service.row('🔀 Разные', 'ℹ️ FAQ')
    bot.send_message(message.from_user.id, 'Для начала нажмите необходимую кнопку', reply_markup=service)

@bot.message_handler(content_types=['text'])
def new_verify(message):
    if message.text.lower() == 'запись нового авто':
        begin_new_car = bot.send_message(message.from_user.id, 'Введите регистрационный номер:')
        bot.register_next_step_handler(begin_new_car, get_car_plate)

def get_car_plate(message):
    global car_plate
    car_plate = message.text.upper()
    bot.send_message(message.from_user.id, 'Введите марку авто:')
    bot.register_next_step_handler(message, get_car_make)

def get_car_make(message):
    global car_make
    car_make = message.text.upper()
    bot.send_message(message.from_user.id, 'Введите модель авто:')
    bot.register_next_step_handler(message, get_car_model)

def get_car_model(message):
    global car_model
    car_model = message.text.upper()
    bot.send_message(message.from_user.id, '1:' + car_plate + '2: ' + car_make + '3: ' + car_model)

bot.polling(none_stop=True)
