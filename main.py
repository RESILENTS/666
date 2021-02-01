import telebot 
from telebot import types
import random
import time

token = '1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def first_q(message):
    service = telebot.types.ReplyKeyboardMarkup(True)
    service.row('Check 1', 'Check 2')
    send = bot.send_message(message.chat.id, 'первый вопрос', reply_markup=service)
    bot.register_next_step_handler(send)
    
def end(message):
    four_answer = message.text
    answers.append(four_answer)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Check 1":
        bot.send_message(message.chat.id, '{}'.format(''.join(answers)))
        
    if message.text == "🤖 Chatex Bot":
        new_pas = "https://t.me/Chatex_bot?start=c_"
        bot.send_message(message.chat.id, new_pas, disable_web_page_preview=True)

bot.polling(none_stop=True)
