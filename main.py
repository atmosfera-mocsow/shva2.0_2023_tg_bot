import os

import telebot
from dotenv import load_dotenv
from telebot.util import quick_markup

load_dotenv()
token = os.environ.get("TOKEN")
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["clear"])
def new_game(message):
    # удаляем результаты пользваотеля
    # ...
    # используем другую функцию
    start_message(message)


@bot.message_handler(commands=["run"])
def run_game(message):
    # отправляем кнопки
    markup = quick_markup(
        {
            "Twitter": {"url": "https://twitter.com", "callback_data": "twitter_pressed"},
            "Facebook": {"url": "https://facebook.com", "callback_data": "facebook_pressed"},
            "Back": {"callback_data": "whatever"},
        },
        row_width=2,
    )
    bot.reply_to(message, "Спасибо, что общаешься со мной")
    bot.send_message(message.chat.id, "Выбирай действие", reply_markup=markup)
    print(message.chat.id)


@bot.message_handler(commands=["start"])
def start_message(message):
    # отправляем сообщения
    bot.send_message(message.chat.id, "Привет ✌️ ")
    bot.send_message(message.chat.id, "Для начала игры нажмите /run")
    print(message.chat.id)


# @bot.callback_query_handler(func=lambda m: True)
# def get_inline_answer(message):
#     print(f"{message=}")
#     bot.send_message(message.chat.id, f"Ого,ты выбрал {message=}")

print("start bot")
bot.infinity_polling()
