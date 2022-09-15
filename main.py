from datetime import datetime
from telebot import types
import telebot
import pytz
import os

# You're supposed to put your TelegramBot token here
#
# os.environ allows you to access the TelegramBot token
# from the environment variable.

bot = telebot.TeleBot(os.environ.get("TELEBOT_TOKEN", "Token here"))

standard_reply = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
standard_reply.add(types.KeyboardButton("🌍 Узнать текущее время"))

@bot.message_handler(commands=['start'])
def start_command(msg):

    bot.send_message(msg.chat.id, "🌍 Здравствуй! \nЭто бот созданный для того чтобы понимать у кого какое время :)", reply_markup=standard_reply)


# This function filters out text messages for the reply keyboard command.
@bot.message_handler(func=lambda msg: msg.text == "🌍 Узнать текущее время")
def current_time(msg):

    african_time = pytz.timezone("Europe/Berlin")
    african_time = datetime.now(african_time)
    african_time = african_time.strftime("%Y-%m-%d %H:%M:%S")

    portland_time = datetime.now(tz=pytz.UTC).replace(microsecond=0)
    portland_time = portland_time.astimezone(pytz.timezone('US/Pacific'))
    portland_time = portland_time.strftime("%Y-%m-%d %H:%M:%S")

    ukrain_time = pytz.timezone("Europe/Kyiv")
    ukrain_time = datetime.now(ukrain_time)
    ukrain_time = ukrain_time.strftime("%Y-%m-%d %H:%M:%S")

    message = f"🕙 Текущее время: \n\n🇪🇺 Европа: {african_time} \n\n🇺🇸 Портленд: {portland_time} \n\n🇺🇦 Украина: {ukrain_time}"
    bot.send_message(msg.chat.id, message)

bot.polling()