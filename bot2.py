import telebot
from telebot import types
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database = "bot"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE Bot")
# mycursor.execute("CREATE TABLE Restaurant (id INT AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(255), Address VARCHAR(255), Latitude FLOAT, Longitude FLOAT, Vegan BOOLEAN, Parking BOOLEAN)")

bot = telebot.TeleBot("1037730141:AAFBEbqNWoBdaEhKKDuKec5H-QjqJAWYwjM")
@bot.message_handler(commands=['calories'])
def type_of_product(message):
    if message.text == '/calories' :
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_mushroom = types.InlineKeyboardButton(text='Mushrooms', callback_data='mushrooms')
        keyboard.add(key_mushroom)  # добавляем кнопку в клавиатуру
        key_sausages = types.InlineKeyboardButton(text='Sausages', callback_data='sausages')
        keyboard.add(key_sausages)
        key_cereals_and_cereals = types.InlineKeyboardButton(text='Cereals and cereals', callback_data='cereals and cereals')
        keyboard.add(key_cereals_and_cereals)  # добавляем кнопку в клавиатуру
        key_oils_and_fats = types.InlineKeyboardButton(text='Oils and Fats', callback_data='Oils and Fats')
        keyboard.add(key_oils_and_fats)
        key_milk_products = types.InlineKeyboardButton(text='Milk products', callback_data='Milk products')
        keyboard.add(key_milk_products)  # добавляем кнопку в клавиатуру
        key_flour_and_flour_products = types.InlineKeyboardButton(text='Flour and flour products', callback_data='Flour and flour products')
        keyboard.add(key_flour_and_flour_products)
        key_meat_products = types.InlineKeyboardButton(text='Meat products', callback_data='Meat products')
        keyboard.add(key_meat_products)  # добавляем кнопку в клавиатуру
        key_vegetables = types.InlineKeyboardButton(text='Vegetables', callback_data='Vegetables')
        keyboard.add(key_vegetables)
        key_nuts_and_dried_fruits = types.InlineKeyboardButton(text='Mushrooms', callback_data='Nuts and dried fruits')
        keyboard.add(key_nuts_and_dried_fruits)  # добавляем кнопку в клавиатуру
        question = "Which product type you want to check?"
        bot.send_message(message.chat.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def all(call):
    def type_of_product(call):
        if call.data == "Milk products":
            keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
            key_milk = types.InlineKeyboardButton(text='Milk 3,2%', callback_data='Milk 3,2%')
            keyboard.add(key_milk)  # добавляем кнопку в клавиатуру
            key_coconut_milk = types.InlineKeyboardButton(text='Coconut milk Aroy-D', callback_data='Coconut milk')
            keyboard.add(key_coconut_milk)
            key_cream_9 = types.InlineKeyboardButton(text='Cream 9%', callback_data='Cream 9%')
            keyboard.add(key_cream_9)  # добавляем кнопку в клавиатуру
            key_cream_20 = types.InlineKeyboardButton(text='Cream 20%', callback_data='Cream 20%')
            keyboard.add(key_cream_20)
            key_sour_cream = types.InlineKeyboardButton(text='Sour cream 25%', callback_data='Sour cream 25%')
            keyboard.add(key_sour_cream)  # добавляем кнопку в клавиатуру
            key_caserole = types.InlineKeyboardButton(text='Cottage cheese casserole', callback_data='Cottage cheese casserole')
            keyboard.add(key_caserole)
            key_kefir = types.InlineKeyboardButton(text='Kefir 2%', callback_data='Kefir 2%')
            keyboard.add(key_kefir)  # добавляем кнопку в клавиатуру
            key_condensed_milk = types.InlineKeyboardButton(text='Сondensed milk', callback_data='Сondensed milk')
            keyboard.add(key_condensed_milk)
            question = 'Choose the product!'
            bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    def get_product(call):
        if call.data == "Milk 3,2%":
            bot.send_message(call.message.chat.id, "Milk 3,2%:\n Proteins, g: 2.9 \n Fats, g: 2.5\n Carbohydrates, g: 4.7 \n Kcal : 52\n")
        if call.data == "Coconut milk":
            bot.send_message(call.message.chat.id, "Coconut milk: \nProteins, g: 1.6 \n Fats, g: 18.5\n Carbohydrates, g: 2.0 \n Kcal : 181\n")
        if call.data == "Cream 9%":
            bot.send_message(call.message.chat.id, "Cream 9%:\n Proteins, g: 2.8 \n Fats, g: 9.0\n Carbohydrates, g: 4.0 \n Kcal : 107\n")
        if call.data == "Cream 20%":
            bot.send_message(call.message.chat.id, "Cream 20%:\nProteins, g: 2.8 \n Fats, g: 20.0\n Carbohydrates, g: 3.7 \n Kcal : 205\n")
        if call.data == "Sour cream 25%":
            bot.send_message(call.message.chat.id, "Sour cream 25%:\nProteins, g: 2.6 \n Fats, g: 25.0\n Carbohydrates, g: 2.5 \n Kcal : 248\n")
        if call.data == "Cottage cheese casserole":
            bot.send_message(call.message.chat.id, "Cottage cheese casserole:\n Proteins, g: 17.6\n Fats, g: 4.2\n Carbohydrates, g: 14.2 \n Kcal : 168\n")
        if call.data == "Kefir 2%":
            bot.send_message(call.message.chat.id, "Kefir 2%:\nProteins, g: 3.4 \n Fats, g: 2.0\n Carbohydrates, g: 4.7 \n Kcal : 50\n")
        if call.data == "Сondensed milk":
            bot.send_message(call.message.chat.id, "Сondensed milk:\nProteins, g: 7.2 \n Fats, g: 8.5\n Carbohydrates, g: 56.0 \n Kcal : 320\n")
    type_of_product(call)
    get_product(call)

@bot.message_handler(content_types=['text'])
def find_restaurant(message):
    if(message.text == "Can you show the cafe next to me?" or message.text == "Can you show the restaurants next to me?"):
        bot.send_message(message.chat.id, "Send your location to me and i will do my best)")


@bot.message_handler(content_types=['location'])
def location(message):
        select = "SELECT * FROM Restaurant WHERE ((Latitude - %s) * (Latitude - %s)) + ((Longitude - %s) * (Longitude - %s)) <= 0.00001417945" % (message.location.latitude, message.location.latitude, message.location.longitude, message.location.longitude)
        mycursor.execute(select)
        myresult = mycursor.fetchall()
        count = "SELECT COUNT(*) FROM Restaurant WHERE ((Latitude - %s) * (Latitude - %s)) + ((Longitude - %s) * (Longitude - %s)) <= 0.00001417945" % (message.location.latitude, message.location.latitude, message.location.longitude, message.location.longitude)
        mycursor.execute(count)
        data = mycursor.fetchall()
        for x in data:
            if x[0] > 0:
                bot.send_message(message.chat.id, "There is " + str(x[0]) + "restaurant near you! Here is their adreses:")
                for adreses in myresult:
                    bot.send_message(message.chat.id, "Restaurant: " + adreses[1] + " Address: " + adreses[2])
            else:
                bot.send_message(message.chat.id, "Sorry, there is not some cafe or restourant near you(")


bot.polling()