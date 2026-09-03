import telebot
import threading
import schedule
import time
import json
import datetime

token = "YOURTELEGRAMBOTTOKEN"
bot = telebot.TeleBot(token)

users = {}
jobs = {}

def save_data():
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

def load_data():
    global users

    try:
        with open("data.json", "r", encoding="utf-8") as file:
            users = json.load(file)
            users = {int(k): v for k, v in users.items()}
        for user_id in users:
            if datetime.datetime.now().strftime("%d.%m.%Y") != users[user_id]["date"]:
                users[user_id]["water"] = 0
                users[user_id]["completed"] = False
                users[user_id]["date"] = datetime.datetime.now().strftime("%d.%m.%Y")
                save_data()

    except FileNotFoundError:
        users = {}

    

def reset_water():
    global users
    for user_id in users:
        users[user_id]["water"] = 0
        users[user_id]["completed"] = False

    save_data()

    print("Счетчики воды сброшены")        

load_data()



@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.chat.id

    today = datetime.datetime.now().strftime("%d.%m.%Y")

    if user_id not in users:
        users[user_id] = {"water": 0, "limit": 2000, "interval": 1, "completed": False, "date": today}

    bot.send_message(
        user_id,
        "Приветствую, я бот который напоминает про питье воды\n\n"
        "'/drank' - сколько ты сейчас выпил(в мл)\n"
        "'/setreminder' - поставить напоминание(в часах)\n"
        "'/stopreminder' - отключить напоминание\n"
        "'/limit' - установить лимит питья(в мл)\n"
        "'/status' - ваш статус"
    )

@bot.message_handler(commands=["limit"])
def limit(message):
    user_id = message.chat.id
    text = message.text.split()

    try:
        amount = int(text[1])
        users[user_id]["limit"] = amount
    except:
        bot.send_message(
            user_id,
            "Например: /limit 2000"
        )
        return
    
    save_data()

    bot.send_message(
        user_id,
        "Лимит установлен"
    )

@bot.message_handler(commands=["drank"])
def drank(message):
    user_id = message.chat.id
    text = message.text.split()

    try:
        amount = int(text[1])
        if amount < 0:
            bot.send_message(
                user_id,
                "Нельзя вводить отрицательное значение"
            )
            return
        users[user_id]["water"] += amount
    except:
        bot.send_message(
            user_id,
            "Например: /drank 300"
        )
        return
    
    save_data()
    
    bot.send_message(
        user_id,
        f"Всего выпито: {users[user_id]["water"]}"
    )

    if users[user_id]["water"] >= users[user_id]["limit"] and not users[user_id]["completed"]:
        bot.send_message(
            user_id,
            f"Поздравляю, вы выполнили дневную норму воды"
        )
        users[user_id]["completed"] = True
        save_data()


@bot.message_handler(commands=["status"])
def status(message):
    user_id = message.chat.id
    left = users[user_id]["limit"] - users[user_id]["water"]
    bot.send_message(
        user_id,
        f"Всего выпито: {users[user_id]["water"]} мл\n"
        f"Осталось выпить: {left} мл"
    )

@bot.message_handler(commands=["setreminder"])
def reminder(message):
    user_id = message.chat.id
    text = message.text.split()

    try:
        amount = int(text[1])
        if amount < 0:
            bot.send_message(
                user_id,
                "Нельзя вводить отрицательное значение"
            )
            return
        users[user_id]["interval"] = amount
    except:
        bot.send_message(
            user_id,
            "Например: /setreminder 1"
        )
        return
    
    if user_id in jobs:
        schedule.cancel_job(jobs[user_id])

    job = schedule.every(users[user_id]["interval"]).hours.do(
        bot.send_message,
        user_id,
        "Пора попить воды!"
    )

    jobs[user_id] = job

    save_data()

    bot.send_message(
        user_id,
        f"Установлено упоминание каждые {amount} часа"
    )

@bot.message_handler(commands=["stopreminder"])
def stopReminder(message):
    user_id = message.chat.id

    if user_id in jobs:
        schedule.cancel_job(jobs[user_id])
        del jobs[user_id]
        users[user_id]["interval"] = None
        save_data()
        bot.send_message(
            user_id,
            "Напоминание отключено"
        )
    else:
        bot.send_message(
            user_id,
            "У вас нету активного напоминания"
        )


def remind():
    while True:
        schedule.run_pending()
        time.sleep(1)

schedule.every().day.at("00:00").do(reset_water)

thread = threading.Thread(target=remind)
thread.daemon = True
thread.start()

bot.polling()
