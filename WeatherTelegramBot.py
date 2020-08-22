# The weather info telegram bot
import telebot
from pyowm import OWM

bot = telebot.TeleBot("your-telegram-token")
owm = OWM('your-API-key')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Welcome")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    city = message.text[0].upper() + message.text[1:] # Делаем первую букву введенного города заглавной
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
	
    answer ="It's " + str.lower(w.status) + " in " + city + " now." + "\n"
    answer += "Average temperature " + str(round(w.temperature('celsius')["temp"]))+ ", feels like " + str(round(w.temperature('celsius')["feels_like"]))
    bot.send_message(message.chat.id,answer)

bot.polling(none_stop=True)