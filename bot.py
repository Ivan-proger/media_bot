from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from time import sleep

#from parser0 import parser_link
#from download import Download

import time
import os


app = Client(
	'mood',
	api_id=2297631,
    api_hash="44c201618c3606df1a58012885311729"
    )
#parser = parser_link()
#result_urls = parser.result_urls
#DOMEN = parser.DOMEN
#i_vid = 1

@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = ""
	typing_symbol = "▓"

	while(tbp != orig_text):
		try:
			msg.edit(tbp + typing_symbol)
			sleep(0.05)

			tbp = tbp + text[0]
			text = text[1:]

			msg.edit(tbp)
			sleep(0.05)

		except FloodWait as e:
			sleep(e.x)

@app.on_message(filters.command("video", prefixes="."))
def code1(app, msg):
	text = "видево"
	msg.edit_text("`" + text + "`")

	try:
		my_dir = os.getcwd()
		j0in = os.path.join(my_dir, 'media')
		os.chdir(j0in)
	except FileNotFoundError:
		print('так это 2 раз')
	finally:
		files = os.listdir(path=os.getcwd())
		file = files[0]
		app.send_video("me", file)

@app.on_message(filters.command("while", prefixes="."))
def code2(app, msg):
	while True:
		result_url = parser.result_url0
		if result_url != result_urls[len(result_urls) - 1]:
			result_urls.append(result_url)
			result_url_print = DOMEN + result_url

			down = Download()
			down.inf0(result_url_print)
			i_vid = down.res

			try:
				my_dir = os.getcwd()
				j0in = os.path.join(my_dir, 'media')
				os.chdir(j0in)
			except FileNotFoundError:
				pass

			down.video_download(result_url_print, i_vid)	
			app.send_video("me", i_vid + ".mp4")


		time.sleep(60)
app.run()
