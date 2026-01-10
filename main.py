from loader import bot
from utils.set_bot_commands import set_default_commands
from database.models import db, User, Programme
from flask import Flask, request
import handlers  # noqa
import telebot


# Flask приложение
app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Telegram bot is running!"


@app.route('/', methods=['POST'])
def get_message():
    data = request.get_json()
    update = telebot.types.Update.de_json(data)
    bot.process_new_updates([update])
    return 'ok'


@app.route('/setup')
def setup():
    bot.set_webhook(url="https://stepan4ik-coder-number-one-bot-a37b.twc1.net/")
    return "Готово! Бот настроен."



db.connect()
db.create_tables([User, Programme], safe=True)

if __name__ == "__main__":
    set_default_commands(bot)
    print("🤖 Бот запускается...")
    bot.remove_webhook()
    app.run(host='0.0.0.0', port=10000, debug=False)
