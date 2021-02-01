from requests import get
import time

def usernameSearch(): 
    twitterurl = 'https://twitter.com/' + username_check_a
    twitterresponse = get(twitterurl, headers=headers)
    if twitterresponse.status_code == 200:
        twitter_i = bot.send_message(message.from_user.id, ' ❌ *Twitter:* Не найдено.', parse_mode='Markdown')
    else:
        twitter_i = bot.send_message(message.from_user.id, ' ➖ *Twitter:* https://twitter.com/' + username_check_a, parse_mode='Markdown')
