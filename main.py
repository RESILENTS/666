 
 ​# -*- coding: utf-8 -*- 
 ​import​ ​telebot 
 ​from​ ​telebot​ ​import​ ​types 
  
 ​bot​ ​=​ ​telebot​.​TeleBot​(​'5108669453:AAGuW4xE9QjnzHH27YRb_6xsZ5-NGuqpgjQ'​) 
  
 ​texttt​ ​=​ ​'текст  ' 
 ​idcanal​ ​=​ айдиканала 
  
 ​@​bot​.​message_handler​(​commands​=​[​'start'​]) 
 ​def​ ​start_message​(​message​): 
 ​        ​userid​ ​=​ ​str​(​message​.​chat​.​id​) 
 ​        ​keyboard​ ​=​ ​types​.​InlineKeyboardMarkup​() 
 ​        ​keyboard​.​add​(​types​.​InlineKeyboardButton​(​text​=​'✔️ Подать заявку'​,​callback_data​=​'податьзаявку'​)) 
 ​        ​bot​.​send_message​(​message​.​chat​.​id​,​"👑 Добро пожаловать в FormatC если ты заинтересован в нашей деятельности то можешь попасть к нам в команду отправив заявку."​,​disable_web_page_preview​ ​=​ ​True​, ​reply_markup​=​keyboard​) 
  
  
 ​@​bot​.​message_handler​(​content_types​=​[​'text'​]) 
 ​def​ ​send_text​(​message​): 
  
 ​        ​if​ ​message​.​text​.​lower​() ​==​ ​''​: 
 ​                ​bot​.​send_message​(​message​.​chat​.​id​, ​texttt​ ,​disable_web_page_preview​ ​=​ ​True​, ​parse_mode​=​'HTML'​) 
  
  
 ​def​ ​add1​(​message​): 
 ​        ​global​ ​m1 
 ​        ​m1​ ​=​ ​message​.​text 
 ​        ​msg​ ​=​ ​bot​.​send_message​(​message​.​chat​.​id​, ​'Сколько времени готовы уделять?'​,​parse_mode​=​'HTML'​) 
 ​        ​bot​.​register_next_step_handler​(​msg​, ​add2​) 
  
 ​def​ ​add2​(​message​): 
 ​        ​global​ ​m2 
 ​        ​m2​ ​=​ ​message​.​text 
 ​        ​msg​ ​=​ ​bot​.​send_message​(​message​.​chat​.​id​, ​'Имеется ли у вас опыт?'​,​parse_mode​=​'HTML'​) 
 ​        ​bot​.​register_next_step_handler​(​msg​, ​add3​) 
  
 ​def​ ​add3​(​message​): 
 ​        ​global​ ​m3 
 ​        ​m3​ ​=​ ​message​.​text 
 ​        ​keyboard​ ​=​ ​types​.​InlineKeyboardMarkup​() 
 ​        ​keyboard​.​add​(​types​.​InlineKeyboardButton​(​text​=​'✔️ Принять'​,​callback_data​=​f'принятьзаявку_​{​message​.​chat​.​id​}​'​)) 
 ​        ​bot​.​send_message​(​idcanal​, ​f'''Имя: @​{​message​.​from_user​.​username​} 
 ​Откуда вы о нас узнали?: ​{​m1​} 
 ​Имеется ли у вас опыт?: ​{​m3​}​'''​,​parse_mode​=​'HTML'​,​reply_markup​=​keyboard​) 
 ​        ​bot​.​send_message​(​message​.​chat​.​id​, ​'Заявка отправлена'​,​parse_mode​=​'HTML'​) 
  
  
 ​@​bot​.​callback_query_handler​(​func​=​lambda​ ​call​:​True​) 
 ​def​ ​podcategors​(​call​): 
  
 ​        ​if​ ​call​.​data​ ​==​ ​'податьзаявку'​: 
 ​                ​msg​ ​=​ ​bot​.​send_message​(​call​.​message​.​chat​.​id​, ​'Откуда вы о нас узнали?'​,​parse_mode​=​'HTML'​) 
 ​                ​bot​.​register_next_step_handler​(​msg​, ​add1​) 
  
  
 ​        ​if​ ​call​.​data​[:​14​] ​==​ ​'принятьзаявку_'​: 
 ​                ​idasd​ ​=​ ​call​.​data​[​14​:] 
 ​                ​bot​.​delete_message​(​chat_id​=​call​.​message​.​chat​.​id​,​message_id​=​call​.​message​.​message_id​) 
 ​                ​main​ ​=​ ​telebot​.​types​.​ReplyKeyboardMarkup​(​True​) 
 ​                ​bot​.​answer_callback_query​(​callback_query_id​=​call​.​id​, ​show_alert​=​True​, ​text​=​"Готово"​) 
 ​                ​bot​.​send_message​(​idasd​,​eply_markup​=​main​) 
 ​                 
  
  
  
 ​bot​.​polling​(​True​)
