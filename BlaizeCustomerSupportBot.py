import telebot
from telebot import types
bot = telebot.TeleBot("6271768191:AAGhP_0qNZBPNSupPtVzsuCaWcOwc_ChLDU")

import openai
openai.api_key = "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"


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!")


@bot.message_handler(commands=['info'])
def start(message):
    bot.send_message(message.from_user.id, message.from_user)


@bot.message_handler()
def get_user_text(message):
    user_name = message.from_user.first_name

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": message.text
            }
        ]
    )

    bot.send_message(message.from_user.id, completion.choices[0].message.content)


bot.polling(none_stop=True)