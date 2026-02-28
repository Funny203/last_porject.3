from config import *
from logic import *

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Расписание на сегодня - покажет уроки на текущий день\nКогда следующий урок - скажет следующий урок",
        reply_markup=get_button()
    )

@bot.message_handler(func=lambda message: True)
def handle(message):
    if message.text == "Расписание на сегодня":
        bot.send_message(message.chat.id, get_schedule_text())
    elif message.text == "Когда следующий урок":
        bot.send_message(message.chat.id, get_time_to_next_lesson())
    else:
        bot.send_message(message.chat.id, "Используй кнопки ниже")

bot.infinity_polling()
