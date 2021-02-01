import telebot 

def handle_text(message):
    if message.text == "🔎 OSINT":
        request = requests.get('https://github.com/')
        if request.status_code == 200:
            bot.send_message(message.chat.id, "+", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "-", parse_mode='Markdown')
