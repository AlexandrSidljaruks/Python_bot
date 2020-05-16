import telebot
import datetime
import pymongo
from pymongo import MongoClient

bot = telebot.TeleBot("1121341438:AAHqPP0EgUJZAjjUDo84GlDusmuomY8LA7k")

# подключение к базе данных
client = MongoClient('localhost', 27017)
# назначение базы
db = client.bot_database
collection = db.bot_collection

@bot.message_handler(commands=['start'])
def print_reminds(message):
    bot.send_message(message.chat.id, "погнали епта")
    remembers = db.posts
    while True:
        d = datetime.datetime.today()
        if remembers.find_one({"when": d}):
            remind_text = remembers.find_one({"when": d})["remind"]
            remind_who = remembers.find_one({"when": d})["who"]
            bot.send_message(message.chat.id, "@" + remind_who + ', ' + "Вы просили напомнить вам " + " " + remind_text)
            remembers.remove({"when" : d, "remind" : remind_text, "who" : remind_who})
            break

@bot.message_handler(commands=['help'])
def print_rules(message):
    bot.send_message(message.chat.id, "Чтобы начать работу с ботом напишите ему команду /start. Команда /help для вызова данного сообщения еще раз.\n"
+ "В нынешнем своем состоянии я буду реагировать на смену аватарки чата и на смену названия чата. Я могу напоминать вам сделать что либо. Для создания напоминания напишите:"
+ " \" (любой ваш текст) напомни (что нужно напомнить) через (кол - во времени) (единицы времени)\n\"Например: \"Напомни купить молока через 20 минут\" ")

@bot.message_handler(content_types=['text'])
def vsegovno(message):
    def remind_me_latter(message):
        s = message.text.lower()
        napomni = s.find("напомни", 0, len(s)) + 8  # находит позицию после слова "напомни" вместе с последующим пробелом
        cherez = s.find("через", 0, len(s)) + 6  # находит позицию после слова "через" вместе с последующим пробелом.
        if (napomni >= 8) and (cherez > 6) and (cherez > napomni):
            # создание словаря для хранения напоминаний и даты + времени привязанных к ним
            # создание, либо подключение к коллекции
            remembers = db.posts
            d = datetime.datetime.today()
            # ассоциативный массив для хранения ключ (время напоминания) : значение (текст напоминания)
            day = 0  # Переменные нужны для вырезки нужных фрагментов строки(найти и отъинтовать дату )
            hour = 0  # переменные day, hour, minute нужны для расчета даты и времени напоминания
            minute = 0  # им будут присвоены отъинтованные значения строки в конкретных случаях

            if (napomni >= 8) and (cherez > 6) and (cherez > napomni):
                # условие выполниться только если бот найдет в строке слова "напомни" и "через", и только если через идет после напомни
                if s.find("дней ", 0, len(s) + 1) >= 0:
                    s1 = s[cherez: len(s) + 1]
                    s1 = s1[: s.find("дней", 0, len(s1) + 1) + 2]
                    day = int(s1)
                    print(day)
                elif s.find("дня", 0, len(s) + 1) >= 0:
                    s1 = s[cherez: len(s) + 1]
                    s1 = s1[: s.find("дня", 0, len(s1) + 1) + 1]
                    day = int(s1)
                    print(day)
                elif s.find("день", 0, len(s) + 1) >= 0:
                    s1 = s[cherez: len(s) + 1]
                    s1 = s1[: s.find("день", 0, len(s1) + 1) + 2]
                    day = int(s1)
                    print(day)
                # блок срабатывает если в тексте находит слово "день" или "дня", т.е. напомни позвонить в кантору через 2 дня
                # блок обрежет строку оставив только кол-во дней и сохранит их отъинтованную величину в переменную "day"
                elif s.find("минут", 0, len(s) + 1) >= 0:
                    s1 = s[cherez: len(s) + 1]
                    s1 = s1[: s.find("минут", 0, len(s1) + 1) + 3]
                    minute = int(s1)
                    print(minute)
                elif s.find("минуты ", 0, len(s) + 1) >= 0:
                    s1 = s[cherez: len(s) + 1]
                    s1 = s1[: s.find("минуты", 0, len(s1) + 1) + 4]
                    minute = int(s1)
                    print(minute)
                elif s.find("минуту  ", 0, len(s) + 1) >= 0:
                    s1 = s[cherez: len(s) + 1]
                    s1 = s1[: s.find("минуту", 0, len(s1) + 1) + 4]
                    hour = int(s1)
                    print(minute)
                # блок срабатывает если в тексте находит слово "минуты", "минут", "минуту" (с пробелом после себя, чтобы знать что это не часть другого слова),
                # т.е. напомни позвонить в кантору через 2 дня
                # блок обрежет строку оставив только кол-во дней и сохранит их отъинтованную величину в переменную "minute"
                elif s.find("часов", 0, len(s) + 1) >= 0:
                    s1 = s[cherez: len(s) + 1]
                    s1 = s1[: s.find("часов", 0, len(s1) + 1) + 3]
                    hour = int(s1)
                    print(hour)
                elif s.find("часа", 0, len(s) + 1) >= 0:
                    s1 = s[cherez: len(s) + 1]
                    s1 = s1[: s.find("часа ", 0, len(s1) + 1) + 2]
                    hour = int(s1)
                    print(hour)
                elif s.find("час", 0, len(s) + 1) >= 0:
                    s1 = s[cherez: len(s) + 1]
                    s1 = s1[: s.find("час ", 0, len(s1) + 1) + 1]
                    hour = int(s1)
                    print(hour)
                # блок срабатывает если в тексте находит слово "часов " или "часа", т.е. напомни позвонить в кантору через 2 дня
                # блок обрежет строку оставив только кол-во дней и сохранит их отъинтованную величину в переменную "day"
                # в данном блоке идет указание новых дат для напоминания
                new_minute = (d.minute + minute) % 60
                new_hour = ((d.hour + hour) + (d.minute + minute) // 60) % 24
                if d.month == 2:
                    # для февраля, идет во внимание только текущий год, потому кол-во дней указано 29
                    new_day = (d.day + day + ((d.hour + hour) + (d.minute + minute) // 60) // 24) % 29
                    new_month = (d.month + (
                                d.day + day + ((d.hour + hour) + (d.minute + minute) // 60) // 24) // 29) % 12
                    new_year = (d.year + (
                            d.month + (d.day + day + ((d.hour + hour) + (d.minute + minute) // 60) // 24) // 29) // 12)
                elif d.month == 1 or d.month == 3 or d.month == 5 or d.month == 7 or d.month == 8 or d.month == 10 or d.month == 12:
                    # перечисление месяцев, в которых по 31 дню
                    new_day = (d.day + day + ((d.hour + hour) + (d.minute + minute) // 60) // 24) % 31
                    new_month = (d.month + (
                                d.day + day + ((d.hour + hour) + (d.minute + minute) // 60) // 24) // 31) % 12
                    new_year = (d.year + (
                            d.month + (d.day + day + ((d.hour + hour) + (d.minute + minute) // 60) // 24) // 31) // 12)
                elif d.month == 4 or d.month == 6 or d.month == 9 or d.month == 11:
                    # перечисление месяцев, в которых по 30 дней
                    new_day = (d.day + day + ((d.hour + hour) + (d.minute + minute) // 60) // 24) % 30
                    new_month = (d.month + (
                                d.day + day + ((d.hour + hour) + (d.minute + minute) // 60) // 24) // 30) % 12
                    new_year = (d.year + (
                            d.month + (d.day + day + ((d.hour + hour) + (d.minute + minute) // 60) // 24) // 30) // 12)
                date_of_member = datetime.datetime(new_year, new_month, new_day, new_hour, new_minute)
                remembers.insert_one(
                    {"when": date_of_member, "remind": s[napomni: cherez - 7], "who": message.from_user.username})
                bot.send_message(message.chat.id, "Так уж и быть, запомню")

    remind_me_latter(message)

    def send_text(message):
        name = message.from_user.first_name
        if message.text.lower() == 'Hi':
            bot.send_message(message.chat.id, 'Привет, ' + name)
        elif message.text.lower() == 'By':
            bot.send_message(message.chat.id, 'Пока, ' + name)

    send_text(message)


@bot.message_handler(content_types=['new_chat_title'])
def ne_ochen(message):
    bot.send_message(message.chat.id, 'Верни как было')


@bot.message_handler(content_types=['new_chat_photo'])
def sssr(message):
    bot.send_message(message.chat.id, 'Раньше было лучше...')


bot.polling()
