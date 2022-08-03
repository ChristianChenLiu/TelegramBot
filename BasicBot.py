import os, telebot
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('BASICBOT_API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Pop'])
def weirdo(message):
    bot.reply_to(message, "Weeb!")

bot.polling()