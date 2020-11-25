from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from time import sleep

import os

app = Client("media")

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

#@app.on_message(filters.command("forw", prefixes="."))
#def cod2(app, msg):



app.run()
