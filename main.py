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
keyboard2.row('Да')
keyboard2.row('Нет')

users = [936565964]
paymentarray = []
    
@bot.message_handler(commands=['start'])
def start_message(message):
    if message.chat.id in users:
    	bot.send_message(message.chat.id,'Authorized',reply_markup=keyboard1)
    else:
    	bot.send_message(message.chat.id,'You are not in whitelist')
@bot.message_handler(commands=['balance'])
def balance(message):
    bot.send_message(message.chat.id, '✅✅✅' + str(api.balance[0]) +'руб✅✅✅')
@bot.message_handler(commands=['pay'])
def payment1(message):
	msg = bot.reply_to(message, 'Введите номер, сумму, комментарий в таком формате: 79998882233|200|coment')
	bot.register_next_step_handler(msg, payment2)
def payment2(message):
	msg = message.text.split('')
	paymentarray.append(msg[0]);paymentarray.append(msg[1]);paymentarray.append(msg[2]);
	msg2 = bot.reply_to(message, 'Вы хотите отправить '+msg[1]+' руб. на номер '+msg[0]+' с комментарием: '+msg[2]+' ?',reply_markup=keyboard2)
	bot.register_next_step_handler(msg2, payment3)
def payment3(message):
	if message.text.lower() == 'да':
		api.pay(account=str(paymentarray[0]), amount=int(paymentarray[1]), comment=str(paymentarray[2])) # я не ебу в каком типе должен быть номер телефона, поэтому если че исправь int на str
		bot.send_message(message.chat.id,'Транзакция проведена!',reply_markup=keyboard1)
		paymentarray.clear()
	elif message.text.lower() == 'нет':
		bot.send_message(message.chat.id,'Отмена транзакции',reply_markup=keyboard1)
		paymentarray.clear()
	else:
		bot.send_message(message.chat.id,'Error',reply_markup=keyboard1)
		paymentarray.clear()
@bot.message_handler(commands=['pay'])
def getbalance(message):
	bot.send_message(message.chat.id,'Your balance: '+str(api.balance[0]),reply_markup=keyboard1)
    
    
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "🤖 BTC Banker":
        request = requests.get('https://github.com/')
        if request.status_code == 200:
            bot.send_message(message.chat.id, "+", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "-", parse_mode='Markdown')
            
    if message.text == "🤖 Chatex Bot":
        request = requests.get('https://github.com/b567567567567')
        if request.status_code == 200:
            bot.send_message(message.chat.id, "+", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "-", parse_mode='Markdown')
        
bot.polling(none_stop=True)
