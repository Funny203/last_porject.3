from config import *
from logic import *


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        wlc_message,
        reply_markup=get_keyboard()
    )

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Получить расписание":
        schedule_text = generate_schedule()
        bot.send_message(
            message.chat.id,
            schedule_text
        )
    else:
        bot.send_message(
            message.chat.id,
            "Используйте кнопку 'Получить расписание'",
            reply_markup=get_keyboard()
        )


if __name__ == "__main__":
    bot.infinity_polling()