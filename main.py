import telebot
import pymysql

import db_work as db
from configs.main_config import *

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    db.new_user_db(message.chat.id, message.from_user.username)
    bot.send_message(message.chat.id, f'Hi, <b>{message.from_user.username}</b>!', parse_mode='html')


@bot.message_handler(commands=['maxim'])
def loh(message):
    if message.chat.id == 1009847133:
        bot.send_message(1009847133, f'Сам себя захуярил', parse_mode='html')
        return
    bot.send_message(1009847133, f'От {message.from_user.username}:\n<b>Максим лох!</b>', parse_mode='html')
    bot.send_message(message.chat.id, f'Поздравление отправлено!', parse_mode='html')


bot.infinity_polling()
