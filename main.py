import lxml
import psycopg2
import telebot
from collections import namedtuple
import requests
from bs4 import BeautifulSoup as bs
from telebot import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE')
conn = psycopg2.connect(dbname='postgres', user='postgres', password='root', host='localhost', port=5433)
cursor = conn.cursor()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет', reply_markup = keyboard())

@bot.message_handler(commands=['stop'])
def start_message(message):
    bot.send_message(message.chat.id, 'Пашел', reply_markup = keyboard())
    get_page_avito('False')



@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == 'AVITO':
        bot.send_message(message.chat.id, 'Ведите ссылку на Avito')
    elif message.text == 'ULA' :
        bot.send_message(message.chat.id, 'ТЫ МОЖЕТ ЕЩЕ ВАНЬКА ВСТАНЬКА ЕПТА?!')
    elif message.text == 'OLX' :
        bot.send_message(message.chat.id, 'ВОТ И НАШЛИ ХОХЛА!')
    elif 'avito.ru' in message.text:
        bot.send_message(message.chat.id, 'Ссылка указана на авито!')
        get_page_avito(message)
    elif 'youla.ru' in message.text:
        bot.send_message(message.chat.id, 'Ссылка на юлу')
        get_page_ula(message)
    elif '.ua' in message.text:
        bot.send_message(message.chat.id, 'Ссылка указана на хохлов!')
        get_page_olx(message)
    else:
        bot.send_message(message.chat.id, 'ТЫ ДУРАК ПИШИ ТО ЧТО ДАЮТ')


def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('AVITO')
    btn2 = types.KeyboardButton('ULA')
    btn3 = types.KeyboardButton('OLX')
    markup.add(btn1, btn2, btn3)
    return markup


def get_page_avito(msg):
    url = msg.text
    name_id = msg.chat.id
    html_text = requests.get(url).text
    soup = bs(html_text, "lxml")
    text_original = soup.find_all('a', {"class":"snippet-link"})
    text_date = soup.find_all('div', attrs={"class":"snippet-date-info"}, text=True)
    for i in text_original:
        for j in text_date:
            if '1 час назад' in j.text:
                date = j.text
                link = i.attrs["href"]
                cursor.execute('INSERT INTO users (user_name, url) VALUES (%s, %s)', (name_id, link))
                conn.commit()
                print(link)
                #delete_quarry = """Delete from users where EXISTS (SELECT * FROM users WHERE (url = %s))"""
                #cursor.execute(delete_quarry, ( link, ))
                #conn.commit()
       # print(i.text + " " + date + "\n")
        #bot.send_message(msg.chat.id, i.text + '\n' "https://www.avito.ru" + i.attrs["href"])


def get_page_ula(msg):
    url = msg.text
    html_text = requests.get(url).text
    soup = bs(html_text, "lxml")
    if 'auto.youla.ru' in url:
        text_original = soup.find_all(attrs={"class":"SerpSnippet_titleWrapper__38bZM"})
        for i in text_original:
            link = i.find('a').get('href')
            print(i.text + '\n' + link)
            bot.send_message(msg.chat.id, i.text + '\n' + link)
    else:
        text_original = soup.find_all("ul", {"class":"product_list _board_items"})
        for i in text_original:
            for j in i.find_all('li', {"class":"product_item"}):
                title = j.find('a').get('title')
                link = j.find('a').get('href')
                print(title + '\n' + "https://youla.ru/" + link)
                bot.send_message(msg.chat.id, title + '\n' + "https://youla.ru/" + link)


def get_page_olx(msg):
    url = msg.text
    html_text = requests.get(url).text
    soup = bs(html_text, 'lxml')
    text_original = soup.find_all('tbody')
    for i in text_original:
        for j in i.find_all('tr', {'class':'wrap'}):
            title = j.find('strong')
            link = j.find('a').get('href')
            print(title.text + '\n' + link)
            #bot.send_message(msg.chat.id, title.text + '\n' + link)


bot.polling(none_stop=True, interval=0)
