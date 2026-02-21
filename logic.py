import telebot
from telebot import types
import random


wlc_message = "Это бот онлайн-школы\nНажмите кнопку ниже чтобы получить расписание."

subjects = ["Математика", "Русский язык", "Английский язык", "Физика", "Химия", 
            "История", "Информатика", "Литература", "Биология", "География", 
            "Обществознание", "Физ-ра", "ОБЗР"]




def generate_schedule():
    lessons = random.randint(4, 6)
    random_subjects = random.sample(subjects, lessons)#random sample рандомайзер без повторений
    schedule = "Расписание уроков на сегодня:\n"
    times = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00"]
    for i in range(lessons):
        schedule += f"{times[i]}-{random_subjects[i]}\n"
        """к изначальной переменной которая состоит из текста 
        добавляется операция сложения переменных(элементов из списка по i) 
        обозначенных фигрной скобкой где i является общим количеством уроков"""
    return schedule


def get_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)#изменение высоты кнопки
    x = types.KeyboardButton("Получить расписание")
    markup.add(x)
    return markup

