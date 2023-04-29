import telebot
from python_aternos import Client


TOKEN="secret"
bot= telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def stapythrt(message):
    bot.send_message(message.chat.id, "Hello, I'm preparing your server")
    aternos = Client.from_credentials('usr', 'pwd')
    servs = aternos.list_servers()
    myserv = servs[0]
    myserv.start()

@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, "Ok, I'm shutting down your server")
    aternos = Client.from_credentials('usr', 'pwd')
    servs = aternos.list_servers()
    myserv = servs[0]
    myserv.stop()




bot.polling()
