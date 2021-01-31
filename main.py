import telebot 
from telebot import types
import random
import time
import requests

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_text(message):
    cid = message.chat.id
    msgPrice = bot.send_message(cid, '✖ Введите желаемый логин для поиска:\n /check')
    bot.register_next_step_handler(msgPrice , step_Set_Price)

@bot.message_handler(commands=['check'])
def step_Set_Price(message):
    cid = message.chat.id
    username = message.text

#searches for usernames
def usernameSearch():
    
    #twitter user search
    twitterurl = 'https://twitter.com/' + username
    twitterresponse = get(twitterurl, headers=headers)
    if twitterresponse.status_code == 200:
        bot.send_message(message.chat.id, "Twitter [-]")
    else:
        bot.send_message(message.chat.id, "Twitter [+]")

    if message.text == "666":
        request = requests.get('https://github.com/')
        if request.status_code == 200:
            bot.send_message(message.chat.id, "https://github.com/", msg2, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, " 666 https://github.com/", msg2, parse_mode='Markdown')
            
    if message.text == "777":
        request = requests.get('https://github.com/b567567567567')
        if request.status_code == 200:
            bot.send_message(message.chat.id, "+", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "-", parse_mode='Markdown')
        
bot.polling(none_stop=True)
