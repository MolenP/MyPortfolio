import telebot
import requests

bot = telebot.TeleBot("8025440437:AAEOFFytLzFbIvIsFl6yAX6lrHwHarxo814")
web_API = "6b994177407e54f62dcfd2b1"

def get_exchange_rate(base_currency, target_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}?apikey={web_API}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and target_currency in data["rates"]:
            return data["rates"][target_currency]
        else:
            return None
    except Exception as e:
        return None

#--------------------Перевод--------------------

texts = {
    "ru": {
        "start": ("Привет, я твой помощник в конвертировании,\nчтобы начать конвертировать, нужно ввести команду '/convert'.\n"
                "Введите команду '/help' для помощи\n"
                "Вы также можете поменять язык командой '/language'"
        ),
        "help": ("Чтобы начать, ты должен ввести команду '/convert'\n. "
                    "Чтобы ввести свою валюту, то ты должен вводить ее вот так 'KZT', 'USD', 'RUB'.\n"
                    "Чтобы остановить бота, нужно ввести фразу 'Stop'\n"
                    "Вы также можете поменять язык командой '/language'"
        ),
        "stop": {
            "language": "Останавливаю изменение языка",
            "convert": "Останавливаю конвертирование"
        },
        "choices": {
            "convert": "Конвертировать",
            "rate": "Узнать курс"
        }, 

        "ChoicesList": ["Конвертировать", "Узнать курс"],

        "preview": "Что вы хотите?",

        "summa": "Введите сумму:",

        "base_currency": "Выберите исходную валюту:",

        "target_currency": "Выберите валюту для перевода:",

        "errors": {
            "language": "Выберите язык с клавиатуры.",
            "choice": "Ошибка: Неизвестная команда",
            "get_amount": "Введите число.",
            "rate": "Ошибка получения курса."
        }
    },
    "en": {
        "start": ("Hi, I'm your conversion assistant.\n To start converting, you need to enter the command '/convert'.\n"
                "Enter the command '/help' for assistance.\n"
                "You can also change the language with the '/language' command."
        ),
        "help": ("To get started, you need to enter the command '/convert'.\n"
                "To enter your currency, you should enter it like this 'KZT', 'USD', 'RUB'.\n"
                "To stop the bot, you need to enter the phrase 'Stop'.\n"
                "You can also change the language with the command '/language'."
        ),
        "stop": {
            "language": "Stopping the language change",
            "convert": "Stopping the conversion"
        },
        "choices": {
            "convert": "Convert", 
            "rate": "Сheck the exchange rate"
        },

        "ChoicesList": ["Convert", "Сheck the exchange rate"],

        "preview": "What do you want?",

        "summa": "Enter the amount:",

        "base_currency": "Choose the base currency:",

        "target_currency": "Choose a currency to transfer:",
        
        "errors": {
            "language": "Choose a language from the keyboard.",
            "choice": "Error: Unknown command",
            "get_amount": "Enter a number.",
            "rate": "Error getting exchange rate."
        }
    }
}

#-----------------------------------------------------------
   
currencies = ["KZT", "USD", "RUB", "EUR", "CNY"]

languages = ["English(Английский)", "Russian(Русский)"]

def create_markup(table):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in table:
        markup.add(item)
    return markup

def get_language(id):
    lang = user_data.get(id, {}).get("language", "ru")
    return lang

user_data = {}

@bot.message_handler(commands=["start"])
def start(message):
    lang = get_language(message.chat.id)

    bot.send_message(message.chat.id, 
                    texts[lang]["start"]
                    )

@bot.message_handler(commands=["help"])
def help(message):
    lang = get_language(message.chat.id)

    bot.send_message(message.chat.id, 
                    texts[lang]["help"]
                    )
    
@bot.message_handler(commands=["language"])
def change_language(message):
    bot.send_message(message.chat.id, 
                    "Выбери один из языков(Choose one of the languages):",
                    reply_markup=create_markup(languages)
                    )
    bot.register_next_step_handler(message, check_language)

def check_language(message):
    lang = get_language(message.chat.id)

    if message.text.lower() == "stop":
        bot.send_message(message.chat.id, 
                        texts[lang]["stop"]["language"]
                        )
        return
    if message.chat.id not in user_data:
        user_data[message.chat.id] = {}

    if message.text == "English(Английский)":
        user_data[message.chat.id]["language"] = "en"
        bot.send_message(message.chat.id, "Language changed to English!")

    elif message.text == "Russian(Русский)":
        user_data[message.chat.id]["language"] = "ru"
        bot.send_message(message.chat.id, "Язык изменен на русский!")

    else:
        bot.send_message(message.chat.id, 
                        texts[lang]["errors"]["language"]
                        )
        bot.register_next_step_handler(message, check_language)



@bot.message_handler(commands=["convert"])
def preview(message):
    lang = get_language(message.chat.id)

    bot.send_message(message.chat.id,
                    texts[lang]["preview"],
                    reply_markup=create_markup(texts[lang]["ChoicesList"])
                    )
    bot.register_next_step_handler(message, check)
    
def check(message):
    lang = get_language(message.chat.id)

    if message.text.lower() == "stop":
        bot.send_message(message.chat.id, 
                        texts[lang]["stop"]["convert"])
        return
    
    elif message.text == "/convert":
        bot.send_message(message.chat.id, 
                        texts[lang]["preview"], 
                        reply_markup=create_markup(texts[lang]["ChoicesList"])
                        )
        bot.register_next_step_handler(message, check)
        return
    
    elif message.text == texts[lang]["choices"]["convert"]:
        bot.send_message(message.chat.id,
                        texts[lang]["summa"])
        bot.register_next_step_handler(message, get_amount)

    elif message.text == texts[lang]["choices"]["rate"]:
        user_data[message.chat.id] = {"amount": 1}
        bot.send_message(message.chat.id, 
                        texts[lang]["base_currency"], 
                        reply_markup=create_markup(currencies)
                        )
        bot.register_next_step_handler(message, get_base_currency)

    else:
        bot.send_message(message.chat.id,
                        texts[lang]["errors"]["choice"], 
                        reply_markup=texts[lang]["ChoicesList"])
        bot.register_next_step_handler(message, check)



def get_amount(message):
    lang = get_language(message.chat.id)

    if message.text.lower() == "stop":
        bot.send_message(message.chat.id, 
                        texts[lang]["stop"]["convert"])
        return
    
    elif message.text == "/convert":
        bot.send_message(message.chat.id, 
                        texts[lang]["preview"], 
                        reply_markup=create_markup(texts[lang]["ChoicesList"])
                        )
        bot.register_next_step_handler(message, check)
        return
    
    try:
        user_data[message.chat.id] = {}
        user_data[message.chat.id]["amount"] = float(message.text)

        bot.send_message(
            message.chat.id,
            texts[lang]["base_currency"],
            reply_markup=create_markup(currencies)
        )

        bot.register_next_step_handler(message, get_base_currency)

    except ValueError:
        bot.send_message(message.chat.id, texts[lang]["errors"]["get_amount"])
        bot.register_next_step_handler(message, get_amount)


def get_base_currency(message):
    lang = get_language(message.chat.id)

    if message.text.lower() == "stop":
        bot.send_message(message.chat.id, 
                        texts[lang]["stop"]["convert"])
        return
    
    elif message.text == "/convert":
        bot.send_message(message.chat.id, 
                        texts[lang]["preview"], 
                        reply_markup=create_markup(texts[lang]["ChoicesList"])
                        )
        bot.register_next_step_handler(message, check)
        return

    user_data[message.chat.id]["base"] = message.text

    bot.send_message(
        message.chat.id,
        texts[lang]["target_currency"],
        reply_markup=create_markup(currencies)
    )

    bot.register_next_step_handler(message, get_target_currency)

def get_target_currency(message):
    lang = get_language(message.chat.id)

    if message.text.lower() == "stop":
        bot.send_message(message.chat.id, 
                        texts[lang]["stop"]["convert"])
        return
    
    elif message.text == "/convert":
        bot.send_message(message.chat.id, 
                        texts[lang]["preview"], 
                        reply_markup=create_markup(texts[lang]["ChoicesList"])
                        )
        bot.register_next_step_handler(message, check)
        return

    user_data[message.chat.id]["target"] = message.text

    amount = user_data[message.chat.id]["amount"]
    base = user_data[message.chat.id]["base"].upper()
    target = user_data[message.chat.id]["target"].upper()

    rate = get_exchange_rate(base, target)

    if rate:
        result = amount * rate
        bot.send_message(
            message.chat.id,
            f"{amount} {base} = {result:.2f} {target}"
        )
    else:
        bot.send_message(
            message.chat.id,
            texts[lang]["errors"]["rate"]
        )

bot.polling()