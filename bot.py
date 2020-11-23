import telebot
import os

bot = telebot.TeleBot('1476611133:AAHHvxmKTElEIaWNRYGVNWEg47TsDhf0jX8')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Видео')
print(keyboard1)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text == 'Видео':
		bot.send_message(message.chat.id, 'Привет, мой создатель')

		try:
			my_dir = os.getcwd()
			j0in = os.path.join(my_dir, 'media')
			os.chdir(j0in)
		except FileNotFoundError:
			print('так это 2 раз')
		finally:
			files = os.listdir(path=os.getcwd())
			file = files[0]
			video = open(file, 'rb')
			bot.send_video(message.chat.id, video)


bot.polling()