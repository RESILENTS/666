import telebot
import time
'''import requests
from time import sleep
token = '988313821:AAEjdtUQK5Z_mUvZgp1W0xnKWpOliIWL6N4'
url = "https://api.telegram.org/bot{token}/"
def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()
def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]
def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id
def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response
def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
            update_id += 1
    sleep(1)
if __name__ == '__main__':
    main()'''
from telebot import types

bot = telebot.TeleBot('1434012352:AAG4yCSwZBi8PafX8hzR9ac7Xd_bNqnIZsE')

emoji_house = u'\U0001F3E0'
emoji_shop = u'\U0001F6CD'
emoji_all = u'\U0001F530'
emoji_order = u'\U0001F6CE'
emoji_menu = u'\U0001F6D2'
emoji_success = u'\U00002705'
emoji_important = u'\U000026A0'
emoji_qiwi = u'\U0001F4B8'
emoji_card = u'\U0001F4B3'
emoji_arrow =u'\U00002B07'
emoji_fail =u'\U0000274C'


keyboard_city = telebot.types.ReplyKeyboardMarkup(True)
keyboard_city.row(emoji_house + 'Москва', emoji_house + 'Санкт-Петербург')
keyboard_city.row(emoji_house + 'Новосибирск', emoji_house + 'Екатеринбург')
keyboard_city.row(emoji_house + 'Нижний Новгород', emoji_house + 'Казань')
keyboard_city.row(emoji_house + 'Челябинск', emoji_house + 'Омск')
keyboard_city.row(emoji_house + 'Самара', emoji_house + 'Ростов-на-Дону')
keyboard_city.row(emoji_house + 'Уфа', emoji_house + 'Красноярск')
keyboard_city.row(emoji_house + 'Пермь', emoji_house + 'Воронеж')
keyboard_city.row(emoji_house + 'Саратов', emoji_house + 'Тюмень')
keyboard_city.row(emoji_house + 'Волгоград', emoji_house + 'Краснодар')
keyboard_city.row(emoji_house + 'Тверь', emoji_house + 'Томск')

keyboard_menu = telebot.types.ReplyKeyboardMarkup(True)
keyboard_menu.row(emoji_all+' Показать все '+emoji_all)
keyboard_menu.row('Марихуана', 'Стимуляторы', 'Эйфоретики')
keyboard_menu.row('Психоделики', 'Экстази', 'Опиаты')


#1
keyboard_mj = telebot.types.ReplyKeyboardMarkup(True)
keyboard_mj.row(emoji_menu + ' К меню')
keyboard_mj.row('Гашиш Euro', 'Шишки AK-47')

#2
keyboard_speed = telebot.types.ReplyKeyboardMarkup(True)
keyboard_speed.row(emoji_menu + ' К меню')
keyboard_speed.row('VHQ Кокаин 98%', 'Амфетамин Белый', 'VHQ A-PVP (Кристаллы)')

#3
keyboard_eiphoria = telebot.types.ReplyKeyboardMarkup(True)
keyboard_eiphoria.row(emoji_menu + ' К меню')
keyboard_eiphoria.row('Мефедрон Мука', 'MDMA / МДМА безводный гидрохлорид')

#4
keyboard_psycho = telebot.types.ReplyKeyboardMarkup(True)
keyboard_psycho.row(emoji_menu + ' К меню')
keyboard_psycho.row('LSD Марки(HQ) 250мкг.')

#5
keyboard_ex = telebot.types.ReplyKeyboardMarkup(True)
keyboard_ex.row(emoji_menu + ' К меню')
keyboard_ex.row('Экстази ТОП ТЕСЛА', 'MDMA 240mg (Красные черепа)')

#6
keyboard_opium = telebot.types.ReplyKeyboardMarkup(True)
keyboard_opium.row(emoji_menu + ' К меню')
keyboard_opium.row('Чистейший Метадон', 'Трамадол х225 (Индия)', 'Героин (Афганистан)')

#All
keyboard_all = telebot.types.ReplyKeyboardMarkup(True)
keyboard_all.row(emoji_menu + ' К меню')
keyboard_all.row('Гашиш Euro', 'Шишки AK-47')
keyboard_all.row('VHQ Кокаин 98%', 'Амфетамин Белый', 'VHQ A-PVP (Кристаллы)')
keyboard_all.row('Мефедрон Мука', 'MDMA / МДМА безводный гидрохлорид')
keyboard_all.row('LSD Марки(HQ) 250мкг.')
keyboard_all.row('Экстази ТОП ТЕСЛА', 'MDMA 240mg (Красные черепа)')
keyboard_all.row('Чистейший Метадон', 'Трамадол х225 (Индия)', 'Героин (Афганистан)')

#Doses
keyboard_dose_gash = telebot.types.ReplyKeyboardMarkup(True)
keyboard_dose_gash.row(emoji_menu + ' К меню')
keyboard_dose_gash.row('0.5 гр. 550 руб.', '1 гр. 900 руб.', '2 гр. 1600 руб.')

keyboard_dose_mj = telebot.types.ReplyKeyboardMarkup(True)
keyboard_dose_mj.row(emoji_menu + ' К меню')
keyboard_dose_mj.row('1 гр. 1300 руб.', '2 гр. 2000 руб.', '5 гр. 4300 руб.')

keyboard_dose_coc = telebot.types.ReplyKeyboardMarkup(True)
keyboard_dose_coc.row(emoji_menu + ' К меню')
keyboard_dose_coc.row('0.5 гр. 4900 руб.', '5 гр. 34900 руб.')

keyboard_dose_amf = telebot.types.ReplyKeyboardMarkup(True)
keyboard_dose_amf.row(emoji_menu + ' К меню')
keyboard_dose_amf.row('0.5 гр. 900 руб.')

keyboard_dose_pvp = telebot.types.ReplyKeyboardMarkup(True)
keyboard_dose_pvp.row(emoji_menu + ' К меню')
keyboard_dose_pvp.row('0.5 гр. 1300 руб.', '1 гр. 2000 руб.', '5 гр. 7600 руб.')

keyboard_dose_mef = telebot.types.ReplyKeyboardMarkup(True)
keyboard_dose_mef.row(emoji_menu + ' К меню')
keyboard_dose_mef.row('1 гр. 1500 руб.', '2 гр. 2500 руб.')

keyboard_dose_mdma = telebot.types.ReplyKeyboardMarkup(True)
keyboard_dose_mdma.row(emoji_menu + ' К меню')
keyboard_dose_mdma.row('0.5 гр. 1700 руб.', '2 гр. 6200 руб.')

keyboard_dose_lsd = telebot.types.ReplyKeyboardMarkup(True)
keyboard_dose_lsd.row(emoji_menu + ' К меню')
keyboard_dose_lsd.row('2 шт. 3000 руб.', '10 шт. 9500 руб.')

keyboard_dose_ex = telebot.types.ReplyKeyboardMarkup(True)
keyboard_dose_ex.row(emoji_menu + ' К меню')
keyboard_dose_ex.row('2 шт. 1600 руб.', '5 шт. 3500 руб.', '10 шт. 5800 руб.')

keyboard_dose_mtd = telebot.types.ReplyKeyboardMarkup(True)
keyboard_dose_mtd.row(emoji_menu + ' К меню')
keyboard_dose_mtd.row('0.25 гр. 1600 руб.', '0.5 гр. 2500 руб.', '1 гр. 4200 руб.')

keyboard_dose_tram = telebot.types.ReplyKeyboardMarkup(True)
keyboard_dose_tram.row(emoji_menu + ' К меню')
keyboard_dose_tram.row('10 шт. 2200 руб.')

keyboard_dose_ger = telebot.types.ReplyKeyboardMarkup(True)
keyboard_dose_ger.row(emoji_menu + ' К меню')
keyboard_dose_ger.row('0.5 гр. 1500 руб.')




keyboard_order = telebot.types.ReplyKeyboardMarkup(True)
keyboard_order.row(emoji_success+'Проверить оплату', emoji_fail+'Отменить заказ')



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выбери свой город:', reply_markup=keyboard_city)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == emoji_house + 'Москва':
        bot.send_message(message.from_user.id, 'Каталог товаров по Москве:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Санкт-Петербург':
        bot.send_message(message.from_user.id, 'Каталог товаров по Санкт-Петербургу:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Новосибирск':
        bot.send_message(message.from_user.id, 'Каталог товаров по Новосибирску:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Екатеринбург':
        bot.send_message(message.from_user.id, 'Каталог товаров по Екатеринбургу:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Нижний Новгород':
        bot.send_message(message.from_user.id, 'Каталог товаров по Нижнему Новгороду:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Казань':
        bot.send_message(message.from_user.id, 'Каталог товаров по Казани:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Челябинск':
        bot.send_message(message.from_user.id, 'Каталог товаров по Челябинску:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Омск':
        bot.send_message(message.from_user.id, 'Каталог товаров по Омску:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Самара':
        bot.send_message(message.from_user.id, 'Каталог товаров по Самаре:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Ростов-на-Дону':
        bot.send_message(message.from_user.id, 'Каталог товаров по Ростову-на-Дону:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Уфа':
        bot.send_message(message.from_user.id, 'Каталог товаров по Уфе:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Красноярск':
        bot.send_message(message.from_user.id, 'Каталог товаров по Красноярску:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Пермь':
        bot.send_message(message.from_user.id, 'Каталог товаров по Перми:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Воронеж':
        bot.send_message(message.from_user.id, 'Каталог товаров по Воронежу:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Волгоград':
        bot.send_message(message.from_user.id, 'Каталог товаров по Волгограду:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Саратов':
        bot.send_message(message.from_user.id, 'Каталог товаров по Саратову:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Тюмень':
        bot.send_message(message.from_user.id, 'Каталог товаров по Тюмени:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Краснодар':
        bot.send_message(message.from_user.id, 'Каталог товаров по Краснодару:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Тверь':
        bot.send_message(message.from_user.id, 'Каталог товаров по Твери:', reply_markup=keyboard_menu)
    elif message.text == emoji_house + 'Томск':
        bot.send_message(message.from_user.id, 'Каталог товаров по Томску:', reply_markup=keyboard_menu)



    elif message.text == emoji_all+' Показать все '+emoji_all:
        bot.send_message(message.from_user.id, 'Весь товар:', reply_markup=keyboard_all)
    elif message.text == 'Марихуана':
        bot.send_message(message.from_user.id, 'Марихуана:', reply_markup=keyboard_mj)
    elif message.text == 'Стимуляторы':
        bot.send_message(message.from_user.id, 'Стимуляторы:', reply_markup=keyboard_speed)
    elif message.text == 'Эйфоретики':
        bot.send_message(message.from_user.id, 'Эйфоретики:', reply_markup=keyboard_eiphoria)
    elif message.text == 'Психоделики':
        bot.send_message(message.from_user.id, 'Психоделики:', reply_markup=keyboard_psycho)
    elif message.text == 'Экстази':
        bot.send_message(message.from_user.id, 'Экстази:', reply_markup=keyboard_ex)
    elif message.text == 'Опиаты':
        bot.send_message(message.from_user.id, 'Опиаты:', reply_markup=keyboard_opium)



    elif message.text == 'Гашиш Euro':
        bot.send_message(message.from_user.id, 'Новая Партия | Легендарный Евро уже не нуждается в представлении!', reply_markup=keyboard_dose_gash)
    elif message.text == 'Шишки AK-47':
        bot.send_message(message.from_user.id, 'Всеми любимый АК47, отец не менее всеми любимого White Russian.', reply_markup=keyboard_dose_mj)


    elif message.text == 'VHQ Кокаин 98%':
        bot.send_message(message.from_user.id, 'Отличный кокаин -FishScale. 0,91+ крэка при варке. Картельная печать.', reply_markup=keyboard_dose_coc)
    elif message.text == 'Амфетамин Белый':
        bot.send_message(message.from_user.id, 'VHQ продукт! Мы - производитель!', reply_markup=keyboard_dose_amf)
    elif message.text == 'VHQ A-PVP (Кристаллы)':
        bot.send_message(message.from_user.id, 'Сертифицированный продукт. Белые прозрачные кристаллы. Высокая степень очистки.', reply_markup=keyboard_dose_pvp)


    elif message.text == 'Мефедрон Мука':
        bot.send_message(message.from_user.id, '99% чистота! Без запаха и жжения! Улучшенная версия легенды', reply_markup=keyboard_dose_mef)
    elif message.text == 'MDMA / МДМА безводный гидрохлорид':
        bot.send_message(message.from_user.id, 'MDMA карамельного оттенка, без примесей MDOH,MDA и пр.', reply_markup=keyboard_dose_mdma)


    elif message.text == 'LSD Марки(HQ) 250мкг.':
        bot.send_message(message.from_user.id, 'Проверенная временем классика, доставка прямиком из Европы', reply_markup=keyboard_dose_lsd)


    elif message.text == 'Экстази ТОП ТЕСЛА':
        bot.send_message(message.from_user.id, 'Экстази с печатью Tesla В одном табле 250мг чистейшего MDMA', reply_markup=keyboard_dose_ex)
    elif message.text == 'MDMA 240mg (Красные черепа)':
        bot.send_message(message.from_user.id, 'MDMA карамельного оттенка, без примесей MDOH,MDA и пр.', reply_markup=keyboard_dose_mdma)


    elif message.text == 'Чистейший Метадон':
        bot.send_message(message.from_user.id, 'Лучший товар! Доступные и лёгкие клады по всему городу!', reply_markup=keyboard_dose_mtd)
    elif message.text == 'Трамадол х225 (Индия)':
        bot.send_message(message.from_user.id, '1 пластина 10 (шт) таблеток! 225 мг активного вещества в каждой таблетке.', reply_markup=keyboard_dose_tram)
    elif message.text == 'Героин (Афганистан)':
        bot.send_message(message.from_user.id, 'Качественный хмурый!', reply_markup=keyboard_dose_ger)



    elif message.text == '0.5 гр. 550 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '1 гр. 900 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '2 гр. 1600 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '1 гр. 1300 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '2 гр. 2000 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '5 гр. 4300 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '0.5 гр. 4900 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '5 гр. 34900 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '0.5 гр. 900 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '0.5 гр. 1300 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '1 гр. 2000 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '5 гр. 7600 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '1 гр. 1500 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '2 гр. 2500 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '0.5 гр. 1700 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '2 гр. 6200 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '2 шт. 3000 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '10 шт. 9500 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '2 шт. 1600 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '5 шт. 3500 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '10 шт. 5800 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '0.25 гр. 1600 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '0.5 гр. 2500 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '1 гр. 4200 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '10 шт. 2200 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)
    elif message.text == '0.5 гр. 1500 руб.':
        bot.send_message(message.from_user.id, 'Инструкция:\n\nДля завершения заказа необходимо оплатить стоимость выбранного товара в течении 20-ти минут с момента получения этого сообщения\n\nСпособы оплаты:\n\n'+emoji_qiwi+'Qiwi: +79255621793\n'+emoji_card+'Картой: (временно нет возможности)\n\n'+'После оплаты заказа вы получаете координаты и фото с места клада\n\nТип клада: магнит\nМестоположение: город, окраина\n\n'+emoji_important+'Важно'+emoji_important+'\nОплачивайте точную стоимость товара\nЗаказ необходимо оплатить в течении 20-ти минут\nПерезаклады только от 5-ти покупок. \nВ качестве исключения и нашей доброй политики вы можете попросить перезаклад, не смотря на эти правила, но лишь в том случае, если ваша ситуация неоднозначная.\n\nЕсли заказ оплачен, нажмите на кнопку проверки\n'+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow+emoji_arrow, reply_markup=keyboard_order)


    elif message.text == emoji_success+'Проверить оплату':
        bot.send_message(message.from_user.id, 'Подождите...')
        time.sleep(4)
        bot.send_message(message.from_user.id, 'Оплата не произведена '+emoji_fail+'\nОплатите Ваш заказ, либо проверьте оплату позднее', reply_markup=keyboard_order)


    elif message.text == emoji_fail + 'Отменить заказ':
        bot.send_message(message.from_user.id, 'Ваш заказ отменен', reply_markup=keyboard_menu)

    elif message.text == emoji_menu + ' К меню':
        bot.send_message(message.from_user.id, 'Меню:', reply_markup=keyboard_menu)

bot.polling()
