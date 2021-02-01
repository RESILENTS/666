import telebot
from telebot import types
import time, os
import requests as r
from random import choice

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

UAs = [  # user agents
    'Mozilla Firefox Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/74.0.3729.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (PlayStation 4 5.55) AppleWebKit/601.2 (KHTML, like Gecko)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
]
username_check_a = ''

def check_response(url):
    response = r.get(url, headers={'User-Agent': choice(UAs)})
    if response.status_code == 200:
        return True
    return False

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
    global username_check_a
    username_check_a = message.text.lower()
    u = username_check_a
    
def instagram(u):
    url = "https://www.instagram.com/" + u
    return check_response(url)

def getResults(message):
    global username_check_a
    username_check_a = message.text.lower()
    u = username_check_a          
    bot.send_message(message.from_user.id, '\nInstagram: ' + ('Found' if instagram(username_check_a) else 'Not found')), parse_mode='Markdown')
        
bot.polling(none_stop=True)
