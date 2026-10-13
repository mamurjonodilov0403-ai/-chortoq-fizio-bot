import telebot

# MANA SHU YERGA YANGI TOKENINGIZNI QOYING - qo'shtirnoq ichiga
TOKEN = "8980768897:AAFoB8U7-JSvRo3LsIjzwm1a-vtnioQRUSA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def salom(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Men Chortoq Fizioterapiya botiman 👨‍⚕️\n\n📍 Sadaf 11, Baynal bog'cha orqasida\n🎁 1-konsultatsiya BEPUL\n📞 99 970-98-43\n\nKanal: @chortoq_fizioterapiya")

print("Bot ishga tushdi... /start deb yozing")
bot.infinity_polling()