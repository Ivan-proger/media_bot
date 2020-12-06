from pyrogram import Client, filters

app = Client(
	'mood',
	api_id=2297631,
    api_hash="44c201618c3606df1a58012885311729"
    )

@app.on_message(filters.me)
def echo(client, message):
	message.reply_text(message.text)

app.run()