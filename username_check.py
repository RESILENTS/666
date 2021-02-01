from requests import get
from classes import username_check_a7
import time

countNullResponse = 0

def Request(query):
    global username_check_a
    result = Connect(query)
    username_check_a += 1
    return username_check_a, result

def usernameSearch(self): 
    global username_check_a
    
    twitterurl = 'https://twitter.com/' + username_check_a
    twitterresponse = get(twitterurl, headers=headers)
    if twitterresponse.status_code == 200:
        twitter_i = bot.send_message(message.from_user.id, ' ❌ *Twitter:* Не найдено.', parse_mode='Markdown')
    else:
        twitter_i = bot.send_message(message.from_user.id, ' ➖ *Twitter:* https://twitter.com/' + username_check_a, parse_mode='Markdown')
