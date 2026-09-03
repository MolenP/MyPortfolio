import telebot
import requests

bot = telebot.TeleBot("YOURTELEGRAMBOTTOKEN")
weather_API = "52a11d2db34547df834164003261906"

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={weather_API}&q={city}&days=3&aqi=no&alerts=no"
    response = requests.get(url)
    data = response.json()

    if not "error" in data:
        forecast = data["forecast"]["forecastday"]
        city_name = data["location"]["name"]
        country = data["location"]["country"]
        weather_report = f"Current weather in 3 days in {city_name}, {country}:\n"
        for day in forecast:
            weather_report += f"{day["date"]}\n" \
                f"Temperature: {day["day"]["avgtemp_c"]}C\n" \
                f"Weather: {day["day"]["condition"]["text"]}\n\n" 
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
