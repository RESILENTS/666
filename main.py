import telebot 
from telebot import types
from requests import get
import time

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'}
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
        bot.register_next_step_handler(username_check, usrchk)

def usrchk(usernamee):
    global username_check_a
    username_check_a = message.text.lower()
                                
        url = "http://www.jeuxvideo.com/profil/{usernamee}"
        r = requests.get(url,headers=headers)
        re = str(r.status_code)
        if "404" in re:
            pass
        elif "200" in re:
            bot.send_message(message.from_user.id, ' ➖ *Twitter:* https://imgur.com/user/' + username_check_a, parse_mode='Markdown')
                                
def user_actions():
    u = input("Username : ")
    usrchk(usernamee=u)
    user_actions()
user_actions()
        
bot.polling(none_stop=True)
