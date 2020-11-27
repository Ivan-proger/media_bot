from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from time import sleep

from parser0 import parser_link

import time
import os

global result_url
global result_urls

app = Client("media")
parser = parser_link()
result_urls = parser.result_urls
result_url = parser.result_url0
DOMEN = parser.DOMEN

@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = ""
	typing_symbol = "}"

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
		video = open(file)
		app.send_video("test_api_bott", file)

@app.on_message(filters.command("while", prefixes="."))
def code2(app, msg):
	while True:
		global result_url
		global result_urls
		time.sleep(2)
		print("2")
		print(result_url)

		if result_url != result_urls[len(result_urls) - 1]:
			result_urls.append(result_url)
			result_url = DOMEN = result_url
			app.send_message('me', result_url)



app.run()
