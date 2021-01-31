import telebot 
from telebot import types
import random
import time
import requests

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/pay')
keyboard1.row('/balance')
keyboard1.row('/history')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('666')
keyboard2.row('777')

users = [936565964]
paymentarray = []
    
@bot.message_handler(commands=['start'])
def payment1(message):
	msg = bot.reply_to(message, 'Введите номер, сумму, комментарий в таком формате: 79998882233|200|coment')
	bot.register_next_step_handler(msg, payment2)
def payment2(message):
	msg = message.text.split()
	paymentarray.append(msg[0]);
	msg2 = bot.reply_to(message, 'Вы хотите отправить руб. на номер '+msg[0]+' с комментарием: ?',reply_markup=keyboard2)
	bot.register_next_step_handler(msg2, payment3)


@bot.message_handler(commands=['pay'])
def payment1(message):
	msg = bot.reply_to(message, 'Введите номер, сумму, комментарий в таком формате: 79998882233|200|coment')
	bot.register_next_step_handler(msg, payment2)
    
    
@bot.message_handler(func=lambda message: True, content_types=['text'])
def payment2(message):
	msg = message.text.split()
	paymentarray.append(msg[0]);
	msg2 = bot.reply_to(message, 'Вы хотите отправить руб. на номер '+msg[0]+' с комментарием: ?',reply_markup=keyboard2)

def handle_text(message):
    if message.text == "666":
        request = requests.get('https://github.com/')
        if request.status_code == 200:
            bot.send_message(message.chat.id, "https://github.com/"  +msg[0], parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, " 666 https://github.com/"  +msg[0], parse_mode='Markdown')
            
    if message.text == "777":
        request = requests.get('https://github.com/b567567567567')
        if request.status_code == 200:
            bot.send_message(message.chat.id, "+", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "-", parse_mode='Markdown')
        
bot.polling(none_stop=True)
