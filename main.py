import telebot
import pymysql
import json

import db_work as db
from configs.main_config import *
import url_updater

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    if db.new_user_db(message.chat.id, message.from_user.username):
        data = {'items': []}
        with open(f'C:\\Users\\schen\\PycharmProject\\pythonProject\\storage\\user_lib\\{message.chat.id}.json', 'w') as outfile:
            json.dump(data, outfile)
    bot.send_message(message.chat.id, f'Hi, <b>{message.from_user.username}</b>!', parse_mode='html')


@bot.message_handler(commands=['new_product'])
def new_product(message):
    bot.send_message(message.chat.id, f'Вставьте ссылку на необходимый продукт:')

    bot.register_next_step_handler(message, url_get)


def url_get(message):
    bot.send_message(message.chat.id, f'Вы ввели: {message.text}')
    res = url_updater.check_template(message.text)
    if res:
        bot.send_message(message.chat.id, f'Найден шаблон: {res}', parse_mode='html')
    else:
        bot.send_message(message.chat.id, f'Все хуйня, давай по-новой', parse_mode='html')


@bot.message_handler(commands=['maxim'])
def loh(message):
    if message.chat.id == 1009847133:
        bot.send_message(1009847133, f'Сам себя захуярил', parse_mode='html')
        return
    bot.send_message(1009847133, f'От {message.from_user.username}:\n<b>Максим лох!</b>', parse_mode='html')
    bot.send_message(message.chat.id, f'Поздравление отправлено!', parse_mode='html')


bot.infinity_polling()
