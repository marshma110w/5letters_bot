import telebot
import bad_solver
import random
import configparser

config = configparser.ConfigParser()
config.read('config.txt')
TOKEN = config['SECRET']['TelebotToken']

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Привет! Это бот для игры "5 букв" от тинков. Вводи в одном сообщении слово и пятибуквенный паттерн из w, b, y.')

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.from_user.id, "Отправляй мне сообщения, типа 'опера wbybb', где w - белый, b - чёрный, y - жёлтый. Чтобы сбросить прогресс угадывания, напиши restart или любую другую строку.")

@bot.message_handler(regexp="[а-яА-Я]{5} [bwy]{5}")
def handle_5letters(message):
    word, pattern = message.text.split()
    print(message)
    bot.send_message(message.from_user.id, "думаю")
    bad_solver.update(message.from_user.id, word, pattern)
    l = bad_solver.find_word(message.from_user.id)
    if len(l) > 10:
        l = random.sample(l, 10)
    bot.send_message(message.from_user.id, 'Попробуй одно из этих:\n' + "\n".join(l))



@bot.message_handler(content_types=['text'])
def handle_other(message):
    bot.reply_to(message, "Сбрасываю историю, угадываем слово сначала...")
    bad_solver.restart(message.from_user.id)



bot.polling(none_stop=True, interval=0)

