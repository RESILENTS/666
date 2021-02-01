import telebot
from telebot import types
from requests import get
import time, os

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
        service2 = telebot.types.ReplyKeyboardMarkup(True)
        service2.row('🔎 Начать поиск')
        username_check = bot.send_message(message.from_user.id, '❗️ Введите ник пользователя без @:', reply_markup=service2)
        bot.register_next_step_handler(username_check, usernameSearch)

def usernameSearch(message):
    headers = {'Mozilla/5.0 (iPhone; CPU iPhone OS 7_2_1 like Mac OS X; en-US) AppleWebKit/534.9.4 (KHTML, like Gecko) Version/4.0.5 Mobile/8B115 Safari/6534.9.4'}
    
    global username_check_a
    username_check_a = message.text.lower()
    
    twitterurl = 'https://imgur.com/user/' + username_check_a
    twitterresponse = get(twitterurl, headers=headers)
    if twitterresponse.status_code == 200:
        bot.send_message(message.from_user.id, ' ❌ *Twitter:* https://imgur.com/user/' + username_check_a, parse_mode='Markdown')
    else:
        bot.send_message(message.from_user.id, ' ➖ *Twitter:* https://imgur.com/user/' + username_check_a, parse_mode='Markdown')
                                
        
bot.polling(none_stop=True)
