import telebot 
from telebot import types
import time

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

username_check_a = ''

@bot.message_handler(commands=['start'])
def start(message):
    service = telebot.types.ReplyKeyboardMarkup(True)
    service.row('🔎 OSINT', '⚙️ Генераторы')
    service.row('🔀 Разные', 'ℹ️ FAQ')
    bot.send_message(message.from_user.id, 'Для начала нажмите необходимую кнопку', reply_markup=service)

@bot.message_handler(commands=['username_check'])
def handle_text(message):
        username_check = bot.send_message(message.from_user.id, '❗️ Введите ник пользователя без @:', reply_markup=service2)
        service2 = telebot.types.ReplyKeyboardMarkup(True)
        service2.row('🔎 Начать поиск')
        bot.register_next_step_handler(username_check, get_car_model)

def get_car_model(message):
    global username_check_a
    username_check_a = message.text.upper()
    
    twitterurl = 'https://twitter.com/' + username_check_a
    twitterresponse = get(twitterurl, headers=headers)
    if twitterresponse.status_code == 200:
        bot.send_message(message.from_user.id, ' ❌ *Twitter:* Не найдено.', parse_mode='Markdown')
    else:
        bot.send_message(message.from_user.id, ' ➖ *Twitter:* https://twitter.com/' + username_check_a, parse_mode='Markdown')
        
bot.polling(none_stop=True)
