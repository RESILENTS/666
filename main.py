import telebot
import time

token = '5108669453:AAGuW4xE9QjnzHH27YRb_6xsZ5-NGuqpgjQ'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.chat.chat_id, "Welcome! Let start, use command /help to see my functional.")

​bot​.​polling​()
