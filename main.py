from​  ​config​ ​import​ ​* 
​from​  ​keyboard​ ​import​ ​* 
  
 ​@​bot​.​message_handler​(​commands​=​[​'start'​]) 
 ​def​ ​start​(​message​): 
 ​    ​chat_id​ ​=​ ​message​.​from_user​.​id 
 ​    ​username​ ​=​ ​message​.​from_user​.​username 
 ​    ​with​ ​sqlite3​.​connect​(​'users.db'​) ​as​ ​conn​: 
 ​        ​cur​ ​=​ ​conn​.​cursor​() 
 ​        ​cur​.​execute​(​"""CREATE TABLE IF NOT EXISTS user(username TEXT, user_id INTEGER);"""​) 
 ​        ​cur​.​execute​(​"SELECT * FROM user WHERE `user_id` = '{}'"​.​format​(​chat_id​)) 
 ​        ​row​ ​=​ ​cur​.​fetchall​() 
 ​        ​if​ ​len​(​row​) ​==​ ​0​: 
 ​            ​cur​.​execute​(​"INSERT INTO `user` (`username`, `user_id`) VALUES(?,?)"​, 
 ​                        (​username​, ​chat_id​,)) 
 ​    ​bot​.​send_message​(​chat_id​, ​f'Добро пожаловать!'​, ​reply_markup​=​main_keyboard​()) 
  
 ​@​bot​.​message_handler​(​commands​=​[​'admin'​]) 
 ​def​ ​admin​(​message​): 
 ​    ​chat_id​ ​=​ ​message​.​from_user​.​id 
 ​    ​if​ ​chat_id​ ​in​ ​admins​: 
 ​        ​bot​.​send_message​(​chat_id​, ​'Вы админ'​, ​reply_markup​=​admin_keyboard​()) 
  
  
 ​@​bot​.​message_handler​(​content_types​=​[​'text'​]) 
 ​def​ ​text​(​message​): 
 ​    ​chat_id​ ​=​ ​message​.​from_user​.​id 
 ​    ​if​ ​message​.​text​ ​==​ ​'Купить iQOS'​: 
 ​        ​inline​ ​=​ ​types​.​ReplyKeyboardMarkup​(​resize_keyboard​=​True​, ​one_time_keyboard​=​False​) 
 ​        ​btn​ ​=​ ​types​.​KeyboardButton​(​text​=​'⭐IQOS 2.4+⭐'​) 
 ​        ​btn2​ ​=​ ​types​.​KeyboardButton​(​text​=​'🌟IQOS 3 DUO🌟'​) 
 ​        ​btn3​ ​=​ ​types​.​KeyboardButton​(​text​=​'🔥IQOS 3 Multi🔥'​) 
 ​        ​btn4​ ​=​ ​types​.​KeyboardButton​(​text​=​'🔙 Назад'​) 
 ​        ​btn5​ ​=​ ​types​.​KeyboardButton​(​text​=​'🔝 Главное Меню'​) 
 ​        ​inline​.​add​(​btn​, ​btn2​) 
 ​        ​inline​.​add​(​btn3​) 
 ​        ​inline​.​add​(​btn4​, ​btn5​) 
 ​        ​bot​.​send_message​(​chat_id​, ​'✨IQOS✨'​, ​reply_markup​=​inline​) 
 ​    ​elif​ ​message​.​text​ ​==​ ​'⭐IQOS 2.4+⭐'​: 
 ​        ​inline​ ​=​ ​types​.​InlineKeyboardMarkup​(​row_width​=​1​) 
 ​        ​btn​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'Купить'​, ​callback_data​=​f'2.4_​{​chat_id​}​'​) 
 ​        ​inline​.​add​(​btn​) 
 ​        ​file​ ​=​ ​open​(​'photo_2020-12-23_20-26-14.jpg'​, ​'rb'​) 
 ​        ​bot​.​send_photo​(​chat_id​, ​file​, 
 ​                       ​caption​=​f'💸 Цена: ​{​price24​}​ руб.​\n​'​, 
 ​                       ​reply_markup​=​inline​) 
 ​        ​file​.​close​() 
 ​    ​elif​ ​message​.​text​ ​==​ ​'🌟IQOS 3 DUO🌟'​: 
 ​        ​inline​ ​=​ ​types​.​InlineKeyboardMarkup​(​row_width​=​1​) 
 ​        ​btn​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'Купить'​, ​callback_data​=​f'3_​{​chat_id​}​'​) 
 ​        ​inline​.​add​(​btn​) 
 ​        ​file​ ​=​ ​open​(​'photo_2020-12-23_20-29-54.jpg'​, ​'rb'​) 
 ​        ​bot​.​send_photo​(​chat_id​, ​file​, 
 ​                       ​caption​=​f'💸 Цена: ​{​price3duo​}​ руб.'​, 
 ​                       ​reply_markup​=​inline​) 
 ​        ​file​.​close​() 
 ​    ​elif​ ​message​.​text​ ​==​ ​'🔥IQOS 3 Multi🔥'​: 
 ​        ​inline​ ​=​ ​types​.​InlineKeyboardMarkup​(​row_width​=​1​) 
 ​        ​btn​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'Купить'​, ​callback_data​=​f'multi_​{​chat_id​}​'​) 
 ​        ​inline​.​add​(​btn​) 
 ​        ​file​ ​=​ ​open​(​'photo_2020-12-23_20-33-03.jpg'​, ​'rb'​) 
 ​        ​bot​.​send_photo​(​chat_id​, ​file​, 
 ​                       ​caption​=​f'💸 Цена: ​{​pricemulti​}​ руб.'​, 
 ​                       ​reply_markup​=​inline​) 
 ​        ​file​.​close​() 
 ​    ​elif​ ​message​.​text​ ​==​ ​'Купить стики HEETS'​: 
 ​        ​inline​ ​=​ ​types​.​InlineKeyboardMarkup​(​row_width​=​1​) 
 ​        ​btn​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'Purple Wave HEETS'​, ​callback_data​=​f'purple_​{​chat_id​}​'​) 
 ​        ​btn1​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'Amber Selection HEETS'​, ​callback_data​=​f'amber_​{​chat_id​}​'​) 
 ​        ​btn2​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'Bronze Selection HEETS'​, ​callback_data​=​f'bronze_​{​chat_id​}​'​) 
 ​        ​btn3​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'Gold Selection HEETS'​, ​callback_data​=​f'gold_​{​chat_id​}​'​) 
 ​        ​btn4​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'Green Zing HEETS'​, ​callback_data​=​f'green_​{​chat_id​}​'​) 
 ​        ​btn5​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'Tropical Swift HEETS'​, ​callback_data​=​f'tropical_​{​chat_id​}​'​) 
 ​        ​btn6​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'Turquoise Selection HEETS'​, ​callback_data​=​f'turq_​{​chat_id​}​'​) 
 ​        ​btn7​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'Yellow Selection HEETS'​, ​callback_data​=​f'bronze_​{​chat_id​}​'​) 
 ​        ​btn8​ ​=​ ​types​.​InlineKeyboardButton​(​text​=​'🔙 Назад'​, ​callback_data​=​f'back_​{​chat_id​}​'​) 
 ​        ​inline​.​add​(​btn​, ​btn1​, ​btn2​, ​btn3​, ​btn4​, ​btn5​, ​btn6​, ​btn7​, ​btn8​) 
 ​        ​bot​.​send_message​(​chat_id​, ​f'Выбирете, цена одной пачки ​{​pricestick​}​ руб.'​, ​reply_markup​=​inline​) 
 ​    ​elif​ ​message​.​text​ ​==​ ​'Рассылка'​ ​and​ ​chat_id​ ​in​ ​admins​: 
 ​        ​message​ ​=​ ​bot​.​send_message​(​chat_id​, ​'💁🏻‍♀️ Введите *сообщение* для рассылки'​, ​parse_mode​=​"Markdown"​) 
 ​        ​bot​.​register_next_step_handler​(​message​, ​add_message​) 
 ​    ​elif​ ​message​.​text​ ​==​ ​'Кол-во пользователей'​ ​and​ ​chat_id​ ​in​ ​admins​: 
 ​        ​with​ ​sqlite3​.​connect​(​'users.db'​) ​as​ ​conn​: 
 ​            ​cur​ ​=​ ​conn​.​cursor​() 
 ​            ​cur​.​execute​(​"SELECT * FROM user"​) 
 ​            ​row​ ​=​ ​cur​.​fetchall​() 
 ​            ​bot​.​send_message​(​message​.​from_user​.​id​, ​'Количество пользователей: '​ ​+​ ​str​(​len​(​row​))) 
 ​    ​elif​ ​message​.​text​ ​==​ ​'Список всех пользователей'​ ​and​ ​chat_id​ ​in​ ​admins​: 
 ​        ​with​ ​sqlite3​.​connect​(​'users.db'​) ​as​ ​conn​: 
 ​            ​cur​ ​=​ ​conn​.​cursor​() 
 ​            ​cur​.​execute​(​"SELECT * from `user`"​) 
 ​            ​row​ ​=​ ​cur​.​fetchall​() 
 ​            ​w_file​ ​=​ ​open​(​"users.csv"​, ​mode​=​"w"​, ​encoding​=​'utf-8'​) 
 ​            ​file_writer​ ​=​ ​csv​.​writer​(​w_file​, ​delimiter​=​","​, ​lineterminator​=​"​\r​"​) 
 ​            ​for​ ​rows​ ​in​ ​row​: 
 ​                ​file_writer​.​writerow​(​rows​) 
 ​            ​w_file​.​close​() 
 ​            ​with​ ​open​(​curdir​ ​+​ ​"/users.csv"​, ​"r"​) ​as​ ​file​: 
 ​                ​bot​.​send_document​(​chat_id​, ​file​) 
 ​    ​elif​ ​message​.​text​ ​==​ ​'Помощь'​: 
 ​        ​bot​.​send_message​(​chat_id​, ​f'Поддержка: ​{​telegram​}​'​) 
 ​    ​elif​ ​message​.​text​ ​==​ ​'🔙 Назад'​: 
 ​        ​bot​.​send_message​(​chat_id​, ​'🔙 Назад'​, ​reply_markup​=​main_keyboard​()) 
 ​    ​elif​ ​message​.​text​ ​==​ ​'🔝 Главное Меню'​: 
 ​        ​bot​.​send_message​(​chat_id​, ​'🔝 Главное Меню'​, ​reply_markup​=​main_keyboard​()) 
  
 ​@​bot​.​callback_query_handler​(​func​=​lambda​ ​call​: ​True​) 
 ​def​ ​call​(​call​): 
 ​    ​puk​ ​=​ ​call​.​data​.​split​(​'_'​) 
 ​    ​if​ ​'2.4'​ ​in​ ​puk​[​0​]: 
 ​        ​chat_id​ ​=​ ​puk​[​1​] 
 ​        ​bot​.​send_message​(​chat_id​, ​f"""➡️После оплаты: 
 ​                Необходимо написать менеджеру данные для отправки. 
 ​                ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️ 
 ​                ФИО. 
 ​                Номер телефона. 
 ​                Город. 
 ​                Номер отделения новой россии. 
 ​                Выбранный вами товар. 
 ​                👤​{​telegram​} 
 ​                ❗️К сообщению прикрепляйте скрин оплаты.❗️"""​) 
 ​        ​price​ ​=​ ​price24 
 ​        ​deposit​(​chat_id​, ​price​) 
 ​    ​elif​ ​'3'​ ​in​ ​puk​[​0​]: 
 ​        ​chat_id​ ​=​ ​puk​[​1​] 
 ​        ​bot​.​send_message​(​chat_id​, ​f"""➡️После оплаты: 
 ​                Необходимо написать менеджеру данные для отправки. 
 ​                ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️ 
 ​                ФИО. 
 ​                Номер телефона. 
 ​                Город. 
 ​                Номер отделения новой россии. 
 ​                Выбранный вами товар. 
 ​                👤​{​telegram​} 
 ​                ❗️К сообщению прикрепляйте скрин оплаты.❗️"""​) 
 ​        ​price​ ​=​ ​price3duo 
 ​        ​deposit​(​chat_id​, ​price​) 
 ​    ​elif​ ​'multi'​ ​in​ ​puk​[​0​]: 
 ​        ​chat_id​ ​=​ ​puk​[​1​] 
 ​        ​bot​.​send_message​(​chat_id​, ​f"""➡️После оплаты: 
 ​                Необходимо написать менеджеру данные для отправки. 
 ​                ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️ 
 ​                ФИО. 
 ​                Номер телефона. 
 ​                Город. 
 ​                Номер отделения новой россии. 
 ​                Выбранный вами товар. 
 ​                👤​{​telegram​} 
 ​                ❗️К сообщению прикрепляйте скрин оплаты.❗️"""​) 
 ​        ​price​ ​=​ ​pricemulti 
 ​        ​deposit​(​chat_id​, ​price​) 
 ​    ​elif​ ​'STATUS-'​ ​in​ ​call​.​data​: 
 ​        ​regex​ ​=​ ​call​.​data​.​split​(​'-'​) 
 ​        ​user_status_pay​(​call​, ​regex​[​1​], ​regex​[​2​]) 
 ​    ​elif​ ​'purple'​ ​in​ ​puk​[​0​]: 
 ​        ​chat_id​ ​=​ ​puk​[​1​] 
 ​        ​bot​.​send_message​(​chat_id​, ​f"""➡️После оплаты: 
 ​                Необходимо написать менеджеру данные для отправки. 
 ​                ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️ 
 ​                ФИО. 
 ​                Номер телефона. 
 ​                Город. 
 ​                Номер отделения новой россии. 
 ​                Выбранный вами товар. 
 ​                👤​{​telegram​} 
 ​                ❗️К сообщению прикрепляйте скрин оплаты.❗️"""​) 
 ​        ​price​ ​=​ ​pricestick 
 ​        ​deposit​(​chat_id​, ​price​) 
 ​    ​elif​ ​'amber'​ ​in​ ​puk​[​0​]: 
 ​        ​chat_id​ ​=​ ​puk​[​1​] 
 ​        ​bot​.​send_message​(​chat_id​, ​f"""➡️После оплаты: 
 ​                Необходимо написать менеджеру данные для отправки. 
 ​                ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️ 
 ​                ФИО. 
 ​                Номер телефона. 
 ​                Город. 
 ​                Номер отделения новой россии. 
 ​                Выбранный вами товар. 
 ​                👤​{​telegram​} 
 ​                ❗️К сообщению прикрепляйте скрин оплаты.❗️"""​) 
 ​        ​price​ ​=​ ​pricestick 
 ​        ​deposit​(​chat_id​, ​price​) 
 ​    ​elif​ ​'bronze'​ ​in​ ​puk​[​0​]: 
 ​        ​chat_id​ ​=​ ​puk​[​1​] 
 ​        ​bot​.​send_message​(​chat_id​, ​f"""➡️После оплаты: 
 ​                Необходимо написать менеджеру данные для отправки. 
 ​                ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️ 
 ​                ФИО. 
 ​                Номер телефона. 
 ​                Город. 
 ​                Номер отделения новой россии. 
 ​                Выбранный вами товар. 
 ​                👤​{​telegram​} 
 ​                ❗️К сообщению прикрепляйте скрин оплаты.❗️"""​) 
 ​        ​price​ ​=​ ​pricestick 
 ​        ​deposit​(​chat_id​, ​price​) 
 ​    ​elif​ ​'gold'​ ​in​ ​puk​[​0​]: 
 ​        ​chat_id​ ​=​ ​puk​[​1​] 
 ​        ​bot​.​send_message​(​chat_id​, ​f"""➡️После оплаты: 
 ​                Необходимо написать менеджеру данные для отправки. 
 ​                ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️ 
 ​                ФИО. 
 ​                Номер телефона. 
 ​                Город. 
 ​                Номер отделения новой россии. 
 ​                Выбранный вами товар. 
 ​                👤​{​telegram​} 
 ​                ❗️К сообщению прикрепляйте скрин оплаты.❗️"""​) 
 ​        ​price​ ​=​ ​pricestick 
 ​        ​deposit​(​chat_id​, ​price​) 
 ​    ​elif​ ​'green'​ ​in​ ​puk​[​0​]: 
 ​        ​chat_id​ ​=​ ​puk​[​1​] 
 ​        ​bot​.​send_message​(​chat_id​, ​f"""➡️После оплаты: 
 ​                Необходимо написать менеджеру данные для отправки. 
 ​                ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️ 
 ​                ФИО. 
 ​                Номер телефона. 
 ​                Город. 
 ​                Номер отделения новой россии. 
 ​                Выбранный вами товар. 
 ​                👤​{​telegram​} 
 ​                ❗️К сообщению прикрепляйте скрин оплаты.❗️"""​) 
 ​        ​price​ ​=​ ​pricestick 
 ​        ​deposit​(​chat_id​, ​price​) 
 ​    ​elif​ ​'tropical'​ ​in​ ​puk​[​0​]: 
 ​        ​chat_id​ ​=​ ​puk​[​1​] 
 ​        ​bot​.​send_message​(​chat_id​, ​f"""➡️После оплаты: 
 ​                Необходимо написать менеджеру данные для отправки. 
 ​                ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️ 
 ​                ФИО. 
 ​                Номер телефона. 
 ​                Город. 
 ​                Номер отделения новой россии. 
 ​                Выбранный вами товар. 
 ​                👤​{​telegram​} 
 ​                ❗️К сообщению прикрепляйте скрин оплаты.❗️"""​) 
 ​        ​price​ ​=​ ​pricestick 
 ​        ​deposit​(​chat_id​, ​price​) 
 ​    ​elif​ ​'turq'​ ​in​ ​puk​[​0​]: 
 ​        ​chat_id​ ​=​ ​puk​[​1​] 
 ​        ​bot​.​send_message​(​chat_id​, ​f"""➡️После оплаты: 
 ​                Необходимо написать менеджеру данные для отправки. 
 ​                ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️ 
 ​                ФИО. 
 ​                Номер телефона. 
 ​                Город. 
 ​                Номер отделения новой россии. 
 ​                Выбранный вами товар. 
 ​                👤​{​telegram​} 
 ​                ❗️К сообщению прикрепляйте скрин оплаты.❗️"""​) 
 ​        ​price​ ​=​ ​pricestick 
 ​        ​deposit​(​chat_id​, ​price​) 
 ​    ​elif​ ​'bronze'​ ​in​ ​puk​[​0​]: 
 ​        ​chat_id​ ​=​ ​puk​[​1​] 
 ​        ​bot​.​send_message​(​chat_id​, ​f"""➡️После оплаты: 
 ​                Необходимо написать менеджеру данные для отправки. 
 ​                ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️ 
 ​                ФИО. 
 ​                Номер телефона. 
 ​                Город. 
 ​                Номер отделения новой россии. 
 ​                Выбранный вами товар. 
 ​                👤​{​telegram​} 
 ​                ❗️К сообщению прикрепляйте скрин оплаты.❗️"""​) 
 ​        ​price​ ​=​ ​pricestick 
 ​        ​deposit​(​chat_id​, ​price​) 
 ​    ​elif​ ​'back'​ ​in​ ​puk​[​0​]: 
 ​        ​bot​.​send_message​(​puk​[​1​], ​'🔙 Назад'​, ​reply_markup​=​main_keyboard​()) 
  
 ​bot​.​polling​()
