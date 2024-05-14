import telebot
from config import TELEGRAM_TOKEN

bot= telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Peluquilla jamao, IG de la minita")

@bot.message_handler(commands=['ig'])
def minita_ig(message):
	bot.reply_to(message, 'IG de la minita: ')

bot.polling()