import telebot
from constant import API_KEY

bot = telebot.Telebot(API_KEY,parse_mode=None)

@bot.message_handler(commands=["help","hello"])
def send_help_message(msg):
    bot.reply_to(message,"hello its me rabin")
bot.polling()
    
