import telebot
import random

TOKEN = '7940730300:AAERe66pq8g4khthtDiU_9_Q5Z6x1v-JjP0'  # вставь сюда свой токен от BotFather
bot = telebot.TeleBot(TOKEN)

games = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Напиши /игра чтобы начать угадывать число 🎲")

@bot.message_handler(commands=['игра'])
def game(message):
    number = random.randint(1, 100)
    games[message.chat.id] = number
    bot.send_message(message.chat.id, "Я загадал число от 1 до 100. Попробуй угадать!")

@bot.message_handler(commands=['сдаться'])
def give_up(message):
    if message.chat.id in games:
        bot.send_message(message.chat.id, f"Окей, я загадал число {games[message.chat.id]} 😅")
        del games[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Ты пока не начал игру. Напиши /игра")

@bot.message_handler(func=lambda m: True)
def guess(message):
    if message.chat.id in games:
        try:
            guess = int(message.text)
            number = games[message.chat.id]
            if guess < number:
                bot.send_message(message.chat.id, "Моё число больше 🔼")
            elif guess > number:
                bot.send_message(message.chat.id, "Моё число меньше 🔽")
            else:
                bot.send_message(message.chat.id, "Ты угадал! 🎉")
                del games[message.chat.id]
        except ValueError:
            bot.send_message(message.chat.id, "Введи число от 1 до 100 😅")
    else:
        bot.send_message(message.chat.id, "Напиши /игра, чтобы начать игру!")

bot.polling()
