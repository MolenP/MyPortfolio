api_key = "AQ.Ab8RN6JzlB7rI2Ie1W9pRs04jXROR5z7oV4zzM12dHnfEHcJFA"

import requests
import telebot

token = "YOURTELEGRAMBOTTOKEN"
bot = telebot.TeleBot(token)

def get_ai_response(message):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

    data = {
        "system_instruction": {
            "parts": [
                {
                    "text": (
                        "Ты наставник по программированию. "
                        "Не давай готовый ответ сразу. "
                        "Сначала дай небольшую подсказку или объясни, "
                        "на что обратить внимание. "
                        "Затем предложи пользователю подумать самому. "
                        "И только после этого покажи правильное решение."
                    )
                }
            ]
        },
        "contents": [
            {
                "parts": [
                    {
                        "text": message
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=data)

    print(response.status_code)

    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "Ошибка Gemini."


def send_long_message(chat_id, text):
    for i in range(0, len(text), 4096):
        bot.send_message(chat_id, text[i:i + 4096])

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    ai_response = get_ai_response(message.text)
    send_long_message(message.chat.id, ai_response)

bot.infinity_polling()
