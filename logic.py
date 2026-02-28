import telebot
import datetime
from config import token
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot(token)

schedule = {
    "Понедельник": ["Математика", "Русский язык", "Английский язык", "Физика", "История"],
    "Вторник": ["Алгебра", "Геометрия", "Литература", "Химия", "Информатика"],
    "Среда": ["Биология", "География", "Обществознание", "Математика", "Английский язык"],
    "Четверг": ["Физика", "Русский язык", "Литература", "История", "ОБЗР"],
    "Пятница": ["Физра", "Информатика", "Химия", "Биология", "География"],
    "Суббота": [],
    "Воскресенье": []
}

lesson_starts = ["09:00", "09:50", "10:40", "11:30", "12:20", "13:10"]
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

def get_schedule_text():
    now = datetime.now()
    today = days[now.weekday()]
    
    if not schedule[today]:
        return f"{today}\nСегодня выходной"
    
    text = f"{today}\n\n"
    for i, lesson in enumerate(schedule[today]):
        text += f"{i+1}. {lesson} ({lesson_starts[i]})\n"
    
    return text

def get_time_to_next_lesson():
    now = datetime.now()
    current_day_index = now.weekday()
    current_time = now.time()
    
    for day_offset in range(7):
        check_day_index = (current_day_index + day_offset) % 7
        check_day = days[check_day_index]
        
        if schedule[check_day]:
            for i in range(len(schedule[check_day])):
                lesson_time = datetime.strptime(lesson_starts[i], "%H:%M").time()
                
                if day_offset == 0 and current_time >= lesson_time:
                    continue
                
                if day_offset == 0:
                    day_text = "сегодня"
                elif day_offset == 1:
                    day_text = "завтра"
                else:
                    day_text = check_day
                
                return f"Следующий урок: {schedule[check_day][i]} ({day_text} в {lesson_starts[i]})"
    
    return "Ближайших уроков нет"

def get_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Расписание на сегодня"))
    markup.add(KeyboardButton("Когда следующий урок"))
    return markup

