import telebot
from telebot import types
import time, os
import requests as r
from random import choice

token = '5108669453:AAGuW4xE9QjnzHH27YRb_6xsZ5-NGuqpgjQ'
bot = telebot.TeleBot(token)

 
 ​from​ ​actions_with_domain​ ​import​ ​domain_url_add_to_bd​, \ 
 ​    ​sql_select_domain​, \ 
 ​    ​delete_domain​, \ 
 ​    ​check_domain_id_and_tg_id​, \ 
 ​    ​delete_domain_url​, ​new_robots_txt​, ​request_api_xml​, ​sql_insert_expired​, ​select_domain 
  
 ​from​ ​profile_sql​ ​import​ ​get_col_domains_from_user​, \ 
 ​    ​get_uptime_for_user​, \ 
 ​    ​get_date_and_domain_expired​, \ 
 ​    ​correctly_telephone​, ​insert_telephone​, ​get_telephone 
  
 ​list_domains​ ​=​ ​"" 
  
 ​bot​ ​=​ ​telebot​.​TeleBot​(​config​.​token​) 
  
  
 ​@​bot​.​message_handler​(​commands​=​[​'start'​]) 
 ​def​ ​get_text_messages​(​message​): 
 ​    ​print​(​message​.​from_user​.​id​) 
 ​    ​print​(​message​.​text​) 
 ​    ​start_menu​ ​=​ ​types​.​ReplyKeyboardMarkup​(​True​, ​True​) 
 ​    ​start_menu​.​row​(​'✅️Добавить сайт'​, ​'❌ Удалить сайт'​) 
 ​    ​start_menu​.​row​(​'🖊️ Перезаписать HASH robots'​, ​'👀 Мой профиль'​) 
 ​    ​bot​.​send_message​(​message​.​chat​.​id​, ​'Стартовое меню'​, ​reply_markup​=​start_menu​) 
  
  
 ​@​bot​.​message_handler​(​content_types​=​[​'text'​]) 
 ​def​ ​handle_text​(​message​): 
 ​    ​user_id​ ​=​ ​message​.​chat​.​id 
 ​    ​if​ ​message​.​text​ ​==​ ​'✅️Добавить сайт'​: 
 ​        ​back_button​ ​=​ ​types​.​ReplyKeyboardMarkup​(​True​, ​True​) 
 ​        ​back_button​.​row​(​'Назад'​) 
 ​        ​print​(​message​.​chat​.​id​) 
 ​        ​print​(​message​.​text​) 
 ​        ​bot​.​send_message​(​message​.​chat​.​id​, 
 ​                         ​f"1️⃣ Пришлите мне адрес домена, который требуется отслеживать.​\n​" 
 ​                         ​f"2️⃣ Я добавлю домен в вашу базу данных и буду проверять его каждые 10 минут.​\n​" 
 ​                         ​f"3️⃣ Мною отслеживаются параметры:​\n​" 
 ​                         ​f"✔️код ответа сервера;​\n​" 
 ​                         ​f"✔️изменения в файле robots.txt;​\n​" 
 ​                         ​f"✔️дата освобождения;​\n​" 
 ​                         ​f"⚠️Если кто-то изменит robots.txt или домен будет недоступен, вы получите уведомление.​\n​" 
 ​                         ​f"<b>Форматы добавления домена:</b>​\n​" 
 ​                         ​f"https://site.ru​\n​" 
 ​                         ​f"http://site.ru​\n​" 
 ​                         ​f"https://www.site.ru"​, 
 ​                         ​reply_markup​=​back_button​, ​parse_mode​=​"HTML"​) 
 ​        ​bot​.​register_next_step_handler​(​message​, ​add_site_bd​) 
  
 ​    ​elif​ ​message​.​text​ ​==​ ​'❌ Удалить сайт'​: 
 ​        ​back_button​ ​=​ ​types​.​ReplyKeyboardMarkup​(​True​, ​True​) 
 ​        ​back_button​.​row​(​'Назад'​) 
 ​        ​print​(​message​.​chat​.​id​) 
 ​        ​print​(​message​.​text​) 
 ​        ​domain_list​ ​=​ ​sql_select_domain​(​user_id​) 
 ​        ​if​ ​len​(​domain_list​) ​>=​ ​1​: 
 ​            ​bot​.​send_message​(​message​.​chat​.​id​, ​text​= 
 ​            ​f"Для <b>удаления</b> сайта требуется указать его <b>ID</b> из указанного ниже списка.​\n​" 
 ​            ​f"👇Ваш список отслеживаемых доменов:👇​\n​" 
 ​            ​f"​{​domain_list​}​\n​" 
 ​            ​f"Укажите ID выбранного домена для удаления"​, ​parse_mode​=​"HTML"​, 
 ​                             ​reply_markup​=​back_button​) 
 ​            ​bot​.​register_next_step_handler​(​message​, ​delete_site_bd​) 
 ​        ​else​: 
 ​            ​bot​.​send_message​(​message​.​chat​.​id​, ​f"Ваш список отслеживаемых доменов пуст 😟​\n​" 
 ​                                              ​f"Для продолжения напишите /start и добавьте новый домен."​) 
  
 ​    ​elif​ ​message​.​text​ ​==​ ​'🖊️ Перезаписать HASH robots'​: 
 ​        ​back_button​ ​=​ ​types​.​ReplyKeyboardMarkup​(​True​, ​True​) 
 ​        ​back_button​.​row​(​'Назад'​) 
 ​        ​print​(​message​.​chat​.​id​) 
 ​        ​print​(​message​.​text​) 
 ​        ​domain_list​ ​=​ ​sql_select_domain​(​user_id​) 
 ​        ​if​ ​len​(​domain_list​) ​>=​ ​1​: 
 ​            ​bot​.​send_message​(​message​.​chat​.​id​, ​f"Ваш список отслеживаемых доменов:​\n​{​domain_list​}​" 
 ​                                              ​f"​\n​Укажите ID выбранного домена для перезаписи robots"​, 
 ​                             ​reply_markup​=​back_button​) 
 ​            ​bot​.​register_next_step_handler​(​message​, ​rewrite_robots_hash​) 
 ​        ​else​: 
 ​            ​bot​.​send_message​(​message​.​chat​.​id​, ​f"Ваш список отслеживаемых доменов пуст 😟​\n​" 
 ​                                              ​f"Для продолжения напишите /start и добавьте новый домен."​) 
  
 ​    ​if​ ​message​.​text​ ​==​ ​'👀 Мой профиль'​: 
 ​        ​back_button​ ​=​ ​types​.​ReplyKeyboardMarkup​(​True​, ​True​) 
 ​        ​actual_telephone_user​ ​=​ ​get_telephone​(​message​.​chat​.​id​) 
 ​        ​if​ ​len​(​actual_telephone_user​) ​==​ ​0​: 
 ​            ​back_button​.​row​(​'Добавить номер телефона (только РФ)'​) 
 ​        ​back_button​.​row​(​'Обратная связь'​) 
 ​        ​back_button​.​row​(​'Назад'​) 
 ​        ​print​(​message​.​chat​.​id​) 
 ​        ​print​(​message​.​text​) 
 ​        ​col​ ​=​ ​get_col_domains_from_user​(​message​.​chat​.​id​) 
  
 ​        ​if​ ​col​ ​==​ ​0​: 
 ​            ​uptime​ ​=​ ​"Недостаточно данных" 
 ​        ​else​: 
 ​            ​uptime​ ​=​ ​get_uptime_for_user​(​message​.​chat​.​id​) 
 ​        ​expired_domain_result_from_user​ ​=​ ​get_date_and_domain_expired​(​message​.​chat​.​id​) 
 ​        ​if​ ​int​(​len​(​expired_domain_result_from_user​)) ​>=​ ​1​: 
 ​            ​domain_name​ ​=​ ​expired_domain_result_from_user​[​'domain_url'​] 
 ​            ​date_expired_domain​ ​=​ ​expired_domain_result_from_user​[​'date_expired'​] 
 ​            ​difference_days​ ​=​ ​expired_domain_result_from_user​[​'difference_days'​] 
 ​        ​else​: 
 ​            ​domain_name​ ​=​ ​"Неизвестно" 
 ​            ​date_expired_domain​ ​=​ ​"Неизвестно" 
 ​            ​difference_days​ ​=​ ​"Неизвестно" 
 ​        ​if​ ​len​(​actual_telephone_user​) ​==​ ​0​: 
 ​            ​actual_telephone_user​ ​=​ ​'Неизвестен' 
 ​        ​bot​.​send_message​(​message​.​chat​.​id​, 
 ​                         ​f"👮 Количество отслеживаемых доменов, шт.: ​{​col​}​\n​" 
 ​                         ​f"🕒 Средний UPTIME по всем доменам: ​{​uptime​}​\n​" 
 ​                         ​f"🌐 Ближайший освобождающийся домен: ​{​domain_name​}​\n​" 
 ​                         ​f"📅 Дата освобождения: ​{​date_expired_domain​}​\n​" 
 ​                         ​f"📅 Дней до освобождения: ​{​difference_days​}​\n​" 
 ​                         ​f"⌛ Интервал проверки доменов, минут: 10​\n​" 
 ​                         ​f"☎️Ваш номер телефона для SMS-уведомлений: ​{​actual_telephone_user​}​\n​"​, 
 ​                         ​reply_markup​=​back_button​) 
 ​        ​# bot.register_next_step_handler(message, add_site_bd) 
 ​    ​elif​ ​message​.​text​ ​==​ ​'Обратная связь'​: 
 ​        ​print​(​message​.​chat​.​id​) 
 ​        ​print​(​message​.​text​) 
 ​        ​back_button​ ​=​ ​types​.​ReplyKeyboardMarkup​(​True​, ​True​) 
 ​        ​back_button​.​row​(​'Назад'​) 
 ​        ​bot​.​send_message​(​message​.​chat​.​id​, ​f"Если у вас возник вопрос " 
 ​                                          ​f"или вы заметили ошибку в работе бота, отправьте нам сообщение. " 
 ​                                          ​f"Мы рассмотрим ваше обращение в течение 24 часов.​\n​" 
 ​                                          ​f"Формат обращения👇​\n​" 
 ​                                          ​f"<b>1️⃣ Ваше имя:</b>​\n​" 
 ​                                          ​f"<b>2️⃣ Описание ошибки или жалоба:</b>"​, 
 ​                         ​reply_markup​=​back_button​, ​parse_mode​=​"HTML"​) 
 ​        ​# bot.register_next_step_handler(message, add_site_bd) 
 ​    ​elif​ ​message​.​text​ ​==​ ​'Добавить номер телефона (только РФ)'​: 
 ​        ​print​(​message​.​chat​.​id​) 
 ​        ​print​(​message​.​text​) 
 ​        ​back_button​ ​=​ ​types​.​ReplyKeyboardMarkup​(​True​, ​True​) 
 ​        ​back_button​.​row​(​'Назад'​) 
 ​        ​bot​.​send_message​(​message​.​chat​.​id​, ​f"Пришлите мне номер телефона в формате <b>7XXXXXXXXXX</b>​\n​" 
 ​                                          ​f"📱 Пример номера: <b>79647489485</b>​\n​" 
 ​                                          ​f"Требуемая длина номера: 11 символов​\n​" 
 ​                                          ​f"Номер должен начинаться с <b>7</b>​\n​" 
 ​                                          ​f"✉️ На указанный номер будут поступать SMS-уведомления о доступности сайтов."​, 
 ​                         ​reply_markup​=​back_button​, ​parse_mode​=​"HTML"​) 
 ​        ​bot​.​register_next_step_handler​(​message​, ​add_telephone​) 
 ​    ​elif​ ​message​.​text​ ​==​ ​'Назад'​: 
 ​        ​print​(​message​.​text​) 
 ​        ​get_text_messages​(​message​) 
  
  
 ​def​ ​add_site_bd​(​message​): 
 ​    ​try​: 
  
 ​        ​if​ ​message​.​text​ ​==​ ​'Назад'​: 
 ​            ​get_text_messages​(​message​) 
 ​        ​else​: 
 ​            ​print​(​"Зашли в else"​) 
 ​            ​user_id​ ​=​ ​message​.​from_user​.​id 
 ​            ​# print(user_id + " User ID") 
 ​            ​print​(​message​.​from_user​.​username​) 
 ​            ​domain_name_telegram​ ​=​ ​message​.​text 
 ​            ​print​(​f"USER ID: ​{​user_id​}​ пытается добавить домен ​{​domain_name_telegram​}​"​) 
 ​            ​status​ ​=​ ​domain_url_add_to_bd​(​domain_name_telegram​, ​user_id​) 
 ​            ​print​(​status​) 
 ​            ​if​ ​status​ ​==​ ​'Success'​: 
 ​                ​expired​ ​=​ ​request_api_xml​(​domain_name_telegram​) 
 ​                ​expired_days​ ​=​ ​expired​[​'difference_days'​] 
 ​                ​expired_date​ ​=​ ​expired​[​'expired_date'​] 
 ​                ​domain​ ​=​ ​select_domain​(​domain_name_telegram​) 
 ​                ​domain_id​ ​=​ ​domain​[​'id'​] 
 ​                ​sql_insert_expired​(​domain_id​, ​expired_date​, ​expired_days​) 
 ​                ​print​(​f"Домен ​{​domain_name_telegram​}​ успешно добавлен в базу данных пользователя ​{​user_id​}​"​) 
 ​                ​bot​.​send_message​(​message​.​from_user​.​id​, 
 ​                                 ​f"🌐 Домен: ​{​domain_name_telegram​}​\n​" 
 ​                                 ​f"✅ Успешно добавлен в базу данных пользователя: ​{​user_id​}​\n​" 
 ​                                 ​f"📅 Количество дней до освобождения домена: ​{​expired_days​}​\n​" 
 ​                                 ​f"Для продолжения напишите /start или нажмите на кнопку 'Назад'"​) 
 ​            ​elif​ ​status​ ​==​ ​"Error1"​: 
 ​                ​bot​.​send_message​(​message​.​from_user​.​id​, 
 ​                                 ​f"⚠ Домен ​{​domain_name_telegram​}​ ранее был добавлен в базу данных.​\n​" 
 ​                                 ​f"Для продолжения напишите /start"​) 
 ​            ​elif​ ​status​ ​==​ ​"Error2"​: 
 ​                ​bot​.​send_message​(​message​.​from_user​.​id​, 
 ​                                 ​f"❌ Код ответа сервера для домена НЕ равен 200 ОК.​\n​" 
 ​                                 ​f"⚠️Проверьте корректность написания доменного имени и его протокола.​\n​" 
 ​                                 ​f"Для продолжения напишите /start"​) 
 ​            ​elif​ ​status​ ​==​ ​"Error0"​: 
 ​                ​delete_domain_url​(​domain_name_telegram​, ​user_id​) 
 ​                ​bot​.​send_message​(​message​.​from_user​.​id​, 
 ​                                 ​f"❌ Ошибка добавления. Ваш сервер заблокировал нашего бота или вы прислали некорректный " 
 ​                                 ​f"домен.​\n​" 
 ​                                 ​f"Скорректируйте работу своего сервера или не добавляйте этот домен.​\n​" 
 ​                                 ​f"Для продолжения напишите /start"​) 
 ​            ​else​: 
 ​                ​bot​.​send_message​(​message​.​from_user​.​id​, ​f"Неизвестная ошибка. Напишите /start"​) 
 ​    ​except​ ​ValueError​: 
 ​        ​bot​.​send_message​(​message​.​from_user​.​id​, ​f"Ошибка добавления домена. Напишите /start"​) 
 ​    ​except​ ​TypeError​: 
 ​        ​bot​.​send_message​(​message​.​from_user​.​id​, ​f"Ошибка добавления домена. Напишите /start"​) 
  
  
 ​def​ ​delete_site_bd​(​message​): 
 ​    ​try​: 
 ​        ​if​ ​message​.​text​ ​==​ ​'Назад'​: 
 ​            ​get_text_messages​(​message​) 
 ​        ​else​: 
 ​            ​domain_id​ ​=​ ​message​.​text 
 ​            ​user_id​ ​=​ ​message​.​from_user​.​id 
 ​            ​print​(​f"Пользователь ​{​user_id​}​ отправил заявку на удаление домена ​{​domain_id​}​ из БД"​) 
 ​            ​len_list_domain​ ​=​ ​check_domain_id_and_tg_id​(​domain_id​, ​user_id​) 
 ​            ​if​ ​int​(​len​(​len_list_domain​)) ​>=​ ​1​: 
 ​                ​delete​ ​=​ ​delete_domain​(​domain_id​, ​user_id​) 
 ​                ​if​ ​delete​ ​==​ ​"Success"​: 
 ​                    ​bot​.​send_message​(​message​.​from_user​.​id​, ​f"Домен ID ​{​domain_id​}​ удален из БД. Продолжить /start"​) 
 ​            ​else​: 
 ​                ​bot​.​send_message​(​message​.​from_user​.​id​, ​f"Указан некорректный id. Напишите /start и повторите команду"​) 
 ​    ​except​ ​ValueError​: 
 ​        ​bot​.​send_message​(​message​.​from_user​.​id​, ​f"Указан некорректный id. Напишите /start и повторите команду"​) 
  
  
 ​def​ ​rewrite_robots_hash​(​message​): 
 ​    ​try​: 
 ​        ​if​ ​message​.​text​ ​==​ ​'Назад'​: 
 ​            ​get_text_messages​(​message​) 
 ​        ​else​: 
 ​            ​domain_id​ ​=​ ​message​.​text 
 ​            ​user_id​ ​=​ ​message​.​from_user​.​id 
 ​            ​print​(​f"Пользователь ​{​user_id​}​ отправил заявку на перезапись robots.txt для домена ​{​domain_id​}​"​) 
 ​            ​len_list_domain​ ​=​ ​check_domain_id_and_tg_id​(​domain_id​, ​user_id​) 
 ​            ​len_list​ ​=​ ​len​(​len_list_domain​) 
 ​            ​if​ ​len_list​ ​>=​ ​1​: 
 ​                ​print​(​len_list_domain​) 
 ​                ​new_robots​ ​=​ ​new_robots_txt​(​len_list_domain​, ​domain_id​) 
 ​                ​if​ ​new_robots​ ​==​ ​'Success'​: 
 ​                    ​print​(​f"ROBOTS.TXT для домена: ​{​len_list_domain​}​ успешно перезаписан."​) 
 ​                    ​bot​.​send_message​(​message​.​from_user​.​id​, 
 ​                                     ​f"ROBOTS.TXT для домена: ​{​len_list_domain​}​ успешно перезаписан."​) 
 ​            ​else​: 
 ​                ​bot​.​send_message​(​message​.​from_user​.​id​, ​f"Указан некорректный id. Напишите /start и повторите команду"​) 
 ​    ​except​ ​ValueError​: 
 ​        ​bot​.​send_message​(​message​.​from_user​.​id​, ​f"Указан некорректный id. Напишите /start и повторите команду"​) 
  
 ​def​ ​add_telephone​(​message​): 
 ​    ​try​: 
 ​        ​if​ ​message​.​text​ ​==​ ​'Назад'​: 
 ​            ​get_text_messages​(​message​) 
 ​        ​else​: 
 ​            ​user_id​ ​=​ ​message​.​from_user​.​id 
 ​            ​print​(​f"Пользователь ​{​user_id​}​ пытается добавить номер телефона"​) 
 ​            ​status_number​ ​=​ ​correctly_telephone​(​message​.​text​) 
 ​            ​print​(​status_number​) 
 ​            ​if​ ​status_number​ ​==​ ​'Error'​: 
 ​                ​bot​.​send_message​(​message​.​from_user​.​id​, ​f"Указан некорректный номер телефона.​\n​" 
 ​                                                       ​f"Напишите /start и повторите команду"​) 
 ​            ​elif​ ​status_number​ ​==​ ​'Success'​: 
 ​                ​insert_telephone​(​message​.​text​, ​user_id​) 
 ​                ​bot​.​send_message​(​message​.​from_user​.​id​, ​f"Номер телефона успешно добавлен в ваш профиль.​\n​"​) 
  
  
  
 ​    ​except​ ​ValueError​: 
 ​        ​bot​.​send_message​(​message​.​from_user​.​id​, ​f"Указан некорректный id. Напишите /start и повторите команду"​) 
  
 ​# Запускаем постоянный опрос бота в Телеграме 
 ​bot​.​polling​(​none_stop​=​True​, ​interval​=​0​) 
 ​#
