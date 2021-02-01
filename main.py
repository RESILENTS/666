import telebot
from telebot import types
from requests import get
import time, os

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
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
    global username_check_a
    username_check_a = message.text.lower()
    
    twitterurl = "https://imgur.com/user/" + username_check_a
    page = requests.get(twitterurl) 
    if page.status_code==200:
        bot.send_message(message.from_user.id, ' ❌ *Twitter:* https://imgur.com/user/' + username_check_a, parse_mode='Markdown')
    else:
        bot.send_message(message.from_user.id, ' ➖ *Twitter:* https://imgur.com/user/' + username_check_a, parse_mode='Markdown')
    
                                
        
bot.polling(none_stop=True)
