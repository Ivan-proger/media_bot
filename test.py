from pyrogram import Client

api_id = 2297631
api_hash = "44c201618c3606df1a58012885311729"
bot_token = "1476611133:AAHHvxmKTElEIaWNRYGVNWEg47TsDhf0jX8"
info = "Greetings from **Heroku**!"

app = Client(":memory:", api_id, api_hash, bot_token=bot_token)

print(info)

@app.on_message()
def work(client, message):
    app.send_message(message.chat.id, info)

app.run()