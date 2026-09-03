import telebot
import requests

bot = telebot.TeleBot("8025440437:AAEOFFytLzFbIvIsFl6yAX6lrHwHarxo814")
weather_API = "52a11d2db34547df834164003261906"

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={weather_API}&q={city}&days=3&aqi=no&alerts=no"
    response = requests.get(url)
    data = response.json()
    print(data)

    if not "error" in data:
        city_name = data["location"]["name"]
        country = data["location"]["country"]
        current = data["current"]
        description = current["condition"]["text"]
        temp = current["temp_c"]
        humidity = current["humidity"]
        wind_speed = current["wind_kph"]
        weather_report = f"Current weather in {city_name}, {country}:\n" \
            f"Description: {description}\n" \
            f"Temperature: {temp}C\n" \
            f"Humidity: {humidity}\n" \
            f"Wind speed: {wind_speed}KPH\n"
        return weather_report
    
    else:
        return "Something went wrong, check correctness of your location"

markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = telebot.types.KeyboardButton("Astana")
item2 = telebot.types.KeyboardButton("Almaty")
item3 = telebot.types.KeyboardButton("Petropavl")
markup.add(item1)
markup.add(item2)
markup.add(item3)

@bot.message_handler(commands=["start"])
def welcome(text):
    bot.send_message(text.chat.id, 
                    "Hello! i'm your helper with weather, do you want to know the weather in your location, write your city here on English with a capital letter",
                    reply_markup=markup)

@bot.message_handler(func=lambda message:True)
def send_weather(message):
    city = message.text
    weather_report = get_weather(city)
    bot.send_message(message.chat.id, weather_report)

bot.polling()